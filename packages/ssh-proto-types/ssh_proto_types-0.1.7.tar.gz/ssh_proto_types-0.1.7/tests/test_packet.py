import ctypes
from typing import Annotated, Any, ClassVar, Self, override

import pytest

import ssh_proto_types
from ssh_proto_types import (
    CustomField,
    Field,
    FieldInfo,
    InvalidHeader,
    Notset,
    Packet,
    Rest,
    get_class_info,
    marshal,
    unmarshal,
)


def test_invalid_field_annotation():
    with pytest.raises(TypeError):

        class InvalidPacket(Packet):
            a: Annotated[float, float]

        print(get_class_info(InvalidPacket))


def test_invalid_field():
    with pytest.raises(TypeError):

        class InvalidPacket(Packet):
            a: Annotated[int, Field(float)]  # pyright: ignore[reportArgumentType]

        print(get_class_info(InvalidPacket))


def test_invalid_parent():
    class InvalidParent(Packet):
        a: int

    with pytest.raises(TypeError):

        class InvalidChild(InvalidParent):  # pyright: ignore[reportUnusedClass]
            b: int


def test_fieldinfo() -> None:
    with pytest.raises(TypeError):
        FieldInfo(
            name="a",
            is_class_var=False,
            is_discriminator=False,
            const_value=Notset.Notset,
            underlaying_type=float,
            overlaying_type=float,
            parser=lambda x: x,
            serializer=lambda x: x,
        )


def test_invalid_type():
    with pytest.raises(TypeError):

        class InvalidPacket(Packet):
            a: float

        print(get_class_info(InvalidPacket))


def test_class_info() -> None:
    class Parent(Packet):
        a: int
        b: bytes

    info = get_class_info(Parent)
    with pytest.raises(ValueError):
        info.get_descriptor_field()


def test_invalid_field_type():
    with pytest.raises(TypeError):

        class InvalidPacket(Packet):
            a: Annotated[int, float, str]

        print(get_class_info(InvalidPacket))


def test_simple_annotatin():
    class SimplePacket(Packet):
        a: Annotated[int, ctypes.c_uint8]
        b: Annotated[bytes, bytes]
        c: Annotated[
            str,
            Field(
                bytes,
                parser=lambda x: x.decode("utf8"),  # pyright: ignore
                serializer=lambda x: x.encode("utf8"),
            ),
        ]
        d: Annotated[int, Field(ctypes.c_uint16)] = 2

    unmarshal(SimplePacket, marshal(SimplePacket(a=1, b=b"hello", c="world")))


def test_invalid_child_discriminator():
    class Parent(Packet):
        version: ClassVar[int]

    with pytest.raises(TypeError):

        class Child(Parent):  # pyright: ignore[reportUnusedClass]
            n: int


def test_strange_order() -> None:
    class StrangeOrderPacket(Packet):
        a: ClassVar[int] = 1
        b: int
        c: ClassVar[str]

    class ChildStrangeOrderPacket(StrangeOrderPacket):
        c: ClassVar[str] = "active"
        d: ClassVar[int] = 2
        e: int

    obj = ChildStrangeOrderPacket(b=1, e=3)
    got = unmarshal(ChildStrangeOrderPacket, marshal(obj))
    assert got == obj


def test_strange_order_2() -> None:
    class StrangeOrderPacket(Packet):
        a: ClassVar[int] = 1
        c: ClassVar[str]

    with pytest.raises(TypeError):

        class ChildStrangeOrderPacket(StrangeOrderPacket):  # pyright: ignore[reportUnusedClass]
            a: ClassVar[int] = 2
            c: ClassVar[str] = "active"


def test_double_discriminator():
    class Parent(Packet):
        version: ClassVar[int] = 1
        mode: ClassVar[str]

    class ChildPacketA(Parent):  # pyright: ignore[reportUnusedClass]
        mode: ClassVar[str] = "active"
        a: int

    with pytest.raises(TypeError):

        class ChildPacketB(Parent):  # pyright: ignore[reportUnusedClass]
            mode: ClassVar[str] = "active"
            b: int


def test_very_illegal_packet():
    class Parent(Packet):
        a: ClassVar[int] = 1
        b: ClassVar[int]

    class ChildPacketA(Packet):
        a: ClassVar[int] = 1
        b: ClassVar[int] = 2

    get_class_info(Parent).children[1] = ChildPacketA

    assert marshal(ChildPacketA()) == b"\x00\x00\x00\x01\x01\x00\x00\x00\x01\x02"
    with pytest.raises(InvalidHeader):
        unmarshal(Parent, b"\x00\x00\x00\x01\x01\x00\x00\x00\x01\x01")


def test_packet_with_rest():
    class RestPacket(Packet):
        a: int
        rest: Annotated[bytes, Rest]  # type: ignore[type-arg]

    obj = RestPacket(a=1, rest=b"restdata")
    got = unmarshal(RestPacket, marshal(obj))
    assert got == obj


class Padding(CustomField[bool]):
    BLOCK_SIZE = 8

    @override
    @classmethod
    def parse(cls, stream: ssh_proto_types.StreamReader, parsed: dict[str, object]) -> bool:
        missing_amount = (cls.BLOCK_SIZE - (stream.amount_read() % cls.BLOCK_SIZE)) % cls.BLOCK_SIZE
        value = stream.read_raw(missing_amount)  # Discard padding bytes
        return value == bytes(range(1, missing_amount + 1))

    @override
    @classmethod
    def serialize(cls, stream: ssh_proto_types.StreamWriter, obj: object, value: bool) -> None:
        if not value:
            raise ValueError("Padding field must be True")

        missing_amount = (cls.BLOCK_SIZE - (len(stream) % cls.BLOCK_SIZE)) % cls.BLOCK_SIZE
        stream.write_raw(bytes(range(1, missing_amount + 1)))  # Write padding bytes


def test_packet_with_padding():
    class PaddingPacket(Packet):
        a: int
        padding: Annotated[bool, Padding]

    obj = PaddingPacket(a=1, padding=True)
    v = marshal(obj)
    assert v == b"\x00\x00\x00\x01\x01\x01\x02\x03"
    got = unmarshal(PaddingPacket, marshal(obj))
    assert got == obj


def test_packet_with_padding_unmarshal():
    class PaddingPacket(Packet):
        a: int
        padding: Annotated[bool, Padding]

    class PaddingPacket2(Packet):
        a: int
        padding: ClassVar[Annotated[bool, Padding]] = True

    valid = b"\x00\x00\x00\x01\x01\x01\x02\x03"
    invalid = b"\x00\x00\x00\x01\x01\x01\x02\x04"

    got = unmarshal(PaddingPacket, valid)
    assert got == PaddingPacket(a=1, padding=True)

    got = unmarshal(PaddingPacket, invalid)
    assert got == PaddingPacket(a=1, padding=False)

    got = unmarshal(PaddingPacket2, valid)
    assert got == PaddingPacket2(a=1)

    with pytest.raises(ValueError):
        unmarshal(PaddingPacket2, invalid)


class Pad(int, CustomField["Pad"]):
    BLOCK_SIZE = 8

    @override
    @classmethod
    def parse(cls, stream: ssh_proto_types.StreamReader, parsed: dict[str, object]) -> "Pad":
        missing_amount = (cls.BLOCK_SIZE - (stream.amount_read() % cls.BLOCK_SIZE)) % cls.BLOCK_SIZE
        value = stream.read_raw(missing_amount)  # Discard padding bytes
        if value != bytes(range(1, missing_amount + 1)):
            raise ValueError("Invalid padding bytes")
        return cls(missing_amount)

    @override
    @classmethod
    def serialize(cls, stream: ssh_proto_types.StreamWriter, obj: object, value: "Pad") -> None:
        missing_amount = (cls.BLOCK_SIZE - (len(stream) % cls.BLOCK_SIZE)) % cls.BLOCK_SIZE
        stream.write_raw(bytes(range(1, missing_amount + 1)))  # Write padding bytes


def test_packet_with_padding_obj():
    class PaddingPacket(Packet):
        a: int
        padding: Pad = Pad(3)

    obj = PaddingPacket(a=1)
    v = marshal(obj)
    assert v == b"\x00\x00\x00\x01\x01\x01\x02\x03"
    got = unmarshal(PaddingPacket, marshal(obj))
    assert got == obj


def test_packet_with_model_marshal():
    class PaddingPacket(Packet):
        a: int
        block_size: int = 8

        def model_marshal(self, stream: ssh_proto_types.StreamWriter) -> None:
            missing_amount = (self.block_size - (len(stream) % self.block_size)) % self.block_size
            stream.write_raw(bytes(range(1, missing_amount + 1)))  # Write padding bytes

        @classmethod
        def model_unmarshal(cls, stream: ssh_proto_types.StreamReader, parsed: dict[str, Any]) -> Self:
            block_size: int = parsed["block_size"]
            missing_amount = (block_size - (stream.amount_read() % block_size)) % block_size
            value = stream.read_raw(missing_amount)  # Discard padding bytes
            if value != bytes(range(1, missing_amount + 1)):
                raise ValueError("Invalid padding bytes")

            return super().model_unmarshal(stream, parsed)

    obj = PaddingPacket(a=1)
    v = marshal(obj)
    assert v == b"\x00\x00\x00\x01\x01\x00\x00\x00\x01\x08\x01\x02\x03\x04\x05\x06"
    assert len(v) % obj.block_size == 0
    got = unmarshal(PaddingPacket, marshal(obj))
    assert got == obj

    obj = PaddingPacket(a=1, block_size=7)
    v = marshal(obj)
    assert v == b"\x00\x00\x00\x01\x01\x00\x00\x00\x01\x07\x01\x02\x03\x04"
    assert len(v) % obj.block_size == 0
    got = unmarshal(PaddingPacket, marshal(obj))
    assert got == obj


def test_packet_uint32():
    class UInt32Packet(Packet):
        a: Annotated[int, ctypes.c_uint32]

    i = get_class_info(UInt32Packet)
    assert i.fields["a"].underlaying_type == ctypes.c_uint32

    obj = UInt32Packet(a=1)
    v = marshal(obj)
    assert v == b"\x00\x00\x00\x01"
    got = unmarshal(UInt32Packet, v)
    assert got == obj
