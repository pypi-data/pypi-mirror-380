import ctypes
from typing import Annotated, ClassVar

import pytest

from ssh_proto_types import (
    Field,
    FieldInfo,
    InvalidHeader,
    Notset,
    Packet,
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
