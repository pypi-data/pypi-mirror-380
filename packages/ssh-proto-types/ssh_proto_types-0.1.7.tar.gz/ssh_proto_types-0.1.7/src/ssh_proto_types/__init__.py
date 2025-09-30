import ctypes
import dataclasses
import enum
import inspect
import typing
from collections.abc import Callable

_SSH_PROTO_TYPE_INFO = "__ssh_proto_type_info__"

__version__ = "0.1.7"


def _is_dataclass(cls: type) -> bool:
    return "__dataclass_params__" in cls.__dict__


def _is_classvar(annotation: type) -> bool:
    origin = typing.get_origin(annotation)
    return origin is typing.ClassVar


class Notset(enum.Enum):
    Notset = enum.auto()


NOTSET = Notset.Notset


class CustomField[T]:
    @classmethod
    def parse(cls, stream: "StreamReader", parsed: dict[str, typing.Any]) -> T:
        raise NotImplementedError()

    @classmethod
    def serialize(cls, stream: "StreamWriter", obj: typing.Any, value: T) -> None:
        raise NotImplementedError()


class Rest(CustomField[bytes]):
    @typing.override
    @classmethod
    def parse(cls, stream: "StreamReader", parsed: dict[str, typing.Any]) -> bytes:
        return stream.read_raw(None)

    @typing.override
    @classmethod
    def serialize(cls, stream: "StreamWriter", obj: typing.Any, value: bytes) -> None:
        stream.write_raw(value)


@dataclasses.dataclass
class FieldInfo[T, U]:
    is_class_var: bool
    is_discriminator: bool
    const_value: U | Notset
    name: str
    underlaying_type: T
    overlaying_type: U
    parser: Callable[[T], U]
    serializer: Callable[[U], T]

    def __post_init__(self):
        if self.underlaying_type not in _UNDERLAYING_TYPES and not issubclass(self.underlaying_type, CustomField):  # type: ignore[call-arg]
            raise TypeError(
                f"Field has unsupported underlaying type {self.underlaying_type}. Supported types are: {_UNDERLAYING_TYPES}"
            )


@dataclasses.dataclass
class _ClassInfo:
    header: bool
    children: dict[typing.Any, type["Packet"]] = dataclasses.field(default_factory=dict[typing.Any, type["Packet"]])
    fields: dict[str, FieldInfo[typing.Any, typing.Any]] = dataclasses.field(
        default_factory=dict[str, FieldInfo[typing.Any, typing.Any]]
    )
    headers: dict[str, typing.Any] = dataclasses.field(default_factory=dict[str, typing.Any])

    def get_descriptor_field(self) -> FieldInfo[typing.Any, typing.Any]:
        for field in self.fields.values():
            if field.is_discriminator:
                return field
        raise ValueError("No discriminator field found")


_UNDERLAYING_TYPES = (
    int,
    bytes,
    str,
    ctypes.c_uint8,
    ctypes.c_uint16,
    ctypes.c_uint32,
    ctypes.c_uint64,
    CustomField,
)

UNDERLAYING_TYPES_T = (
    int | bytes | str | ctypes.c_uint8 | ctypes.c_uint16 | ctypes.c_uint32 | ctypes.c_uint64 | CustomField[typing.Any]
)


@dataclasses.dataclass
class Field:
    type: type[UNDERLAYING_TYPES_T]
    parser: Callable[[UNDERLAYING_TYPES_T], typing.Any] | None = None
    serializer: Callable[[typing.Any], UNDERLAYING_TYPES_T] | None = None

    def __post_init__(self):
        if self.type not in _UNDERLAYING_TYPES:
            raise TypeError(
                f"Field has unsupported underlaying type {self.type}. Supported types are: {_UNDERLAYING_TYPES}"
            )


def _process_field(cls: type, name: str, annotation: type) -> FieldInfo[typing.Any, typing.Any]:
    is_class_var = _is_classvar(annotation)
    if is_class_var:
        annotation = typing.get_args(annotation)[0]

    const_value: typing.Any | Notset = NOTSET
    if is_class_var and hasattr(cls, name):
        const_value = getattr(cls, name)

    is_discriminator = is_class_var and const_value is NOTSET

    if typing.get_origin(annotation) is typing.Annotated:
        args = typing.get_args(annotation)
        overlaying_type, args = args[0], args[1:]
        if len(args) == 1 and not isinstance(args[0], Field):
            underlaying_type = args[0]

            def _parser_simple(x: typing.Any):
                return overlaying_type(x)

            _underlaying_type = underlaying_type
            if _underlaying_type in (
                ctypes.c_uint8,
                ctypes.c_uint16,
                ctypes.c_uint32,
                ctypes.c_uint64,
            ):
                _underlaying_type = int

            if issubclass(_underlaying_type, CustomField):
                return FieldInfo(
                    name=name,
                    underlaying_type=underlaying_type,  # type: ignore
                    overlaying_type=overlaying_type,
                    parser=None,  # type: ignore
                    serializer=None,  # type: ignore
                    is_class_var=is_class_var,
                    is_discriminator=is_discriminator,
                    const_value=const_value,
                )

            def _serializer_simple(x: typing.Any):
                return _underlaying_type(x)

            return FieldInfo(
                name=name,
                underlaying_type=underlaying_type,
                overlaying_type=overlaying_type,
                parser=_parser_simple,
                serializer=_serializer_simple,
                is_class_var=is_class_var,
                is_discriminator=is_discriminator,
                const_value=const_value,
            )
        else:
            for arg in args:
                if isinstance(arg, Field):
                    underlaying_type = arg.type

                    _underlaying_type = underlaying_type
                    if _underlaying_type in (
                        ctypes.c_uint8,
                        ctypes.c_uint16,
                        ctypes.c_uint32,
                        ctypes.c_uint64,
                    ):
                        _underlaying_type = int

                    if issubclass(_underlaying_type, CustomField):
                        return FieldInfo(
                            name=name,
                            underlaying_type=underlaying_type,
                            overlaying_type=overlaying_type,
                            parser=None,  # type: ignore
                            serializer=None,  # type: ignore
                            is_class_var=is_class_var,
                            is_discriminator=is_discriminator,
                            const_value=const_value,
                        )

                    def _parser_adv(x: typing.Any):
                        return overlaying_type(x)

                    def _serializer_adv(x: typing.Any):
                        return _underlaying_type(x)

                    parser = arg.parser if arg.parser is not None else _parser_adv
                    serializer = arg.serializer if arg.serializer is not None else _serializer_adv
                    return FieldInfo(
                        name=name,
                        underlaying_type=underlaying_type,
                        overlaying_type=overlaying_type,
                        parser=parser,
                        serializer=serializer,
                        is_class_var=is_class_var,
                        is_discriminator=is_discriminator,
                        const_value=const_value,
                    )
            else:
                raise TypeError(
                    f"Field {name} in class {cls.__name__} has invalid Annotated type. When using typing.Annotated, you must provide a Field instance as one of the arguments."
                )

    return FieldInfo(
        name=name,
        underlaying_type=annotation,
        overlaying_type=annotation,
        parser=lambda x: x,
        serializer=lambda x: x,
        is_class_var=is_class_var,
        is_discriminator=is_discriminator,
        const_value=const_value,
    )


def _process_class(cls: "type[Packet]") -> None:
    if _is_dataclass(cls):
        return

    fields: dict[str, FieldInfo[typing.Any, typing.Any]] = {}
    annotations = inspect.get_annotations(cls)
    for name, annotation in annotations.items():
        fields[name] = _process_field(cls, name, annotation)

    parent = get_parent_class(cls)
    combined_fields: dict[str, FieldInfo[typing.Any, typing.Any]] = {}
    if parent is None:
        combined_fields = fields
    else:
        parent_info = get_class_info(parent)
        for name, field in parent_info.fields.items():
            if field.is_discriminator:
                if name not in fields:
                    raise TypeError(
                        f"Class {cls.__name__} is missing discriminator field {name} from parent class {parent.__name__}"
                    )
                else:
                    combined_fields[name] = fields.pop(name)
            else:
                if name in fields:
                    raise TypeError(
                        f"Class {cls.__name__} is overriding field {name} from parent class {parent.__name__} with a new value, which is not allowed"
                    )

                else:
                    combined_fields[name] = field
        for name, field in fields.items():
            combined_fields[name] = field

    header = any(x.is_discriminator for x in combined_fields.values())

    info = _ClassInfo(header=header, fields=combined_fields)

    parent = get_parent_class(cls)
    if parent is not None:
        parent_info = get_class_info(parent)
        if not parent_info.header:
            raise TypeError(
                "Class {cls.__name__} has parent class {parent.__name__} which is not a header class, but {cls.__name__} is a header class."
            )
        descriptor_field = parent_info.get_descriptor_field()
        descriptor_value = getattr(cls, descriptor_field.name)
        if descriptor_value in parent_info.children:
            raise TypeError(
                f"Class {cls.__name__} has descriptor value {descriptor_value} for field {descriptor_field.name}, but this value is already used by class {parent_info.children[descriptor_value].__name__}"
            )
        parent_info.children[descriptor_value] = cls

    setattr(cls, _SSH_PROTO_TYPE_INFO, info)

    cls = dataclasses.dataclass(slots=True, kw_only=True)(cls)


@typing.dataclass_transform(kw_only_default=True)
class Packet:
    def __init_subclass__(cls: "type[Packet]") -> None:
        _process_class(cls)

    @classmethod
    def model_unmarshal(cls, stream: "StreamReader", parsed: dict[str, typing.Any]) -> typing.Self:
        return cls(**parsed)  # type: ignore[call-arg]

    def model_marshal(self, stream: "StreamWriter") -> None:
        pass


def is_packet(cls: type) -> bool:
    return hasattr(cls, _SSH_PROTO_TYPE_INFO)


def get_class_info(cls: Packet | type[Packet]) -> _ClassInfo:
    return getattr(cls, _SSH_PROTO_TYPE_INFO)


def get_parent_class(cls: type[Packet]) -> type[Packet] | None:
    if is_packet(cls.__bases__[0]):
        return cls.__bases__[0]
    return None


@dataclasses.dataclass
class StreamWriter:
    data: bytearray = dataclasses.field(default_factory=bytearray)
    offset: int = 0

    def write_uint8(self, value: int) -> None:
        self.data.append(value & 0xFF)

    def write_uint16(self, value: int) -> None:
        self.data.extend(value.to_bytes(2, "big"))

    def write_uint32(self, value: int) -> None:
        self.data.extend(value.to_bytes(4, "big"))

    def write_uint64(self, value: int) -> None:
        self.data.extend(value.to_bytes(8, "big"))

    def write_bytes(self, value: bytes) -> None:
        self.write_uint32(len(value))
        self.data.extend(value)

    def write_mpint(self, value: int) -> None:
        if value == 0:
            self.write_bytes(b"")
            return
        byte_length = value.bit_length() // 8 + 1
        byte_data = value.to_bytes(byte_length, "big", signed=True)
        self.write_bytes(byte_data)

    def write_string(self, value: str) -> None:
        b = value.encode("utf-8")
        self.write_bytes(b)

    def write_raw(self, value: bytes) -> None:
        self.data.extend(value)

    @typing.overload
    def write(
        self,
        ctype: type[ctypes.c_uint8 | ctypes.c_uint16 | ctypes.c_uint32 | ctypes.c_uint64 | int],
        value: int,
    ) -> None: ...

    @typing.overload
    def write(self, ctype: type[bytes | Rest], value: bytes) -> None: ...

    @typing.overload
    def write(self, ctype: type[str], value: str) -> None: ...

    def write(self, ctype: type[UNDERLAYING_TYPES_T], value: int | bytes | str) -> None:
        match ctype:
            case c if c is ctypes.c_uint8:
                self.write_uint8(value)  # type: ignore[arg-type]
            case c if c is ctypes.c_uint16:
                self.write_uint16(value)  # type: ignore[arg-type]
            case c if c is ctypes.c_uint32:
                self.write_uint32(value)  # type: ignore[arg-type]
            case c if c is ctypes.c_uint64:
                self.write_uint64(value)  # type: ignore[arg-type]
            case c if c is int:
                self.write_mpint(value)  # type: ignore[arg-type]
            case c if c is bytes:
                self.write_bytes(value)  # type: ignore[arg-type]
            case c if c is str:
                self.write_string(value)  # type: ignore[arg-type]
            case _:
                raise TypeError(f"Unsupported type {ctype} for writing")

    def get_bytes(self) -> bytes:
        return bytes(self.data[self.offset :])

    def __len__(self) -> int:
        return len(self.data) - self.offset


@dataclasses.dataclass
class StreamReader:
    data: memoryview | bytes
    _idx: int = 0
    offset: int = 0

    @property
    def idx(self) -> int:
        return self._idx + self.offset

    @idx.setter
    def idx(self, value: int) -> None:
        self._idx = value - self.offset

    def _get_slice(self, length: int) -> bytes:
        if self.idx + length > len(self.data):
            raise EOFError("Not enough data to read")
        value = self.data[self.idx : self.idx + length]
        self.idx += length
        return bytes(value)

    def read_uint8(self) -> int:
        data = self._get_slice(1)
        return data[0]

    def read_uint16(self) -> int:
        data = self._get_slice(2)
        return int.from_bytes(data, "big")

    def read_uint32(self) -> int:
        data = self._get_slice(4)
        return int.from_bytes(data, "big")

    def read_uint64(self) -> int:
        data = self._get_slice(8)
        return int.from_bytes(data, "big")

    def read_bytes(self) -> bytes:
        length = self.read_uint32()
        data = self._get_slice(length)
        return data

    def read_mpint(self) -> int:
        data = self.read_bytes()
        return int.from_bytes(data, "big", signed=True)

    def read_string(self) -> str:
        data = self.read_bytes()
        return data.decode("utf-8")

    def read_raw(self, length: int | None) -> bytes:
        if length is None:
            length = len(self.data) - self.idx
        data = self._get_slice(length)
        return data

    def read(self, ctype: type[UNDERLAYING_TYPES_T]) -> int | bytes | str | Rest:
        match ctype:
            case c if c is ctypes.c_uint8:
                return self.read_uint8()
            case c if c is ctypes.c_uint16:
                return self.read_uint16()
            case c if c is ctypes.c_uint32:
                return self.read_uint32()
            case c if c is ctypes.c_uint64:
                return self.read_uint64()
            case c if c is int:
                return self.read_mpint()
            case c if c is bytes:
                return self.read_bytes()
            case c if c is str:
                return self.read_string()
            case _:
                raise TypeError(f"Unsupported type {ctype} for reading")

    def eof(self) -> bool:
        return self.idx >= len(self.data)

    def __len__(self) -> int:
        return len(self.data) - self.idx

    def amount_read(self) -> int:
        return self._idx


class InvalidHeader(RuntimeError):
    pass


def _unmarshal_field(
    stream: StreamReader,
    field: FieldInfo[typing.Any, typing.Any],
    parsed: dict[str, typing.Any],
) -> typing.Any:
    if field.name in parsed:
        print(f"Field {field.name} already parsed, skipping")
        if field.const_value is not NOTSET and parsed[field.name] != field.const_value:
            raise InvalidHeader(
                f"Field {field.name} has constant value {field.const_value}, but got {parsed[field.name]}"
            )
        return parsed[field.name]
    if issubclass(field.underlaying_type, CustomField):
        value = field.underlaying_type.parse(stream, parsed)  # type: ignore[arg-type]
        parsed[field.name] = value
    else:
        value = stream.read(field.underlaying_type)
        value = field.parser(value)
    parsed[field.name] = value
    if field.const_value is not NOTSET and value != field.const_value:
        raise ValueError(f"Field {field.name} has constant value {field.const_value}, but got {value}")
    return value  # type: ignore[return-value]


def _unmarshal[T: Packet](
    stream: StreamReader, cls: type[T], parsed: dict[str, typing.Any]
) -> tuple[dict[str, typing.Any], type[T]]:
    info = get_class_info(cls)

    for field in info.fields.values():
        _unmarshal_field(stream, field, parsed)

    child_cls = cls
    if info.header:
        descriptor_field = info.get_descriptor_field()
        descriptor_value = parsed[descriptor_field.name]
        if descriptor_value not in info.children:
            raise ValueError(
                f"Unknown descriptor value {descriptor_value} for field {descriptor_field.name} in class {cls.__name__}"
            )
        child_cls = info.children[descriptor_value]
        parsed, child_cls = _unmarshal(stream, child_cls, parsed)
    return parsed, typing.cast(type[T], child_cls)


def unmarshal[T: Packet](cls: type[T], data: bytes | StreamReader) -> T:
    stream = (
        StreamReader(data.data, offset=data.idx) if isinstance(data, StreamReader) else StreamReader(memoryview(data))
    )
    parsed, cls = _unmarshal(stream, cls, {})

    for field in get_class_info(cls).fields.values():
        if field.is_class_var:
            del parsed[field.name]

    obj = cls.model_unmarshal(stream, parsed)  # type: ignore[call-arg]

    if isinstance(data, StreamReader):
        data.idx = stream.idx

    return obj


def marshal(obj: Packet, stream: StreamWriter | None = None) -> bytes:
    info = get_class_info(obj)
    if info.header:
        raise ValueError("Cannot marshal header class directly")
    _stream = StreamWriter() if stream is None else StreamWriter(stream.data, offset=len(stream))  # type: ignore[arg-type]
    for field in info.fields.values():
        value = getattr(obj, field.name)
        if issubclass(field.underlaying_type, CustomField):
            field.underlaying_type.serialize(_stream, obj, value)  # type: ignore[arg-type]
        else:
            value = field.serializer(value)  # Validate serialization
            _stream.write(field.underlaying_type, value)

    obj.model_marshal(_stream)

    return _stream.get_bytes()
