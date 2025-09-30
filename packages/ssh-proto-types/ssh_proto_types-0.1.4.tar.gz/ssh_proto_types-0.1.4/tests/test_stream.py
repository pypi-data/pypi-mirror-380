import ctypes
from typing import Any

import pytest

from ssh_proto_types import Rest, StreamReader, StreamWriter

testdata_writer: list[tuple[type, Any, bytes]] = [
    (ctypes.c_uint8, 1, b"\x01"),
    (ctypes.c_uint16, 1, b"\x00\x01"),
    (ctypes.c_uint32, 1, b"\x00\x00\x00\x01"),
    (ctypes.c_uint64, 1, b"\x00\x00\x00\x00\x00\x00\x00\x01"),
    (ctypes.c_uint8, 2**8 - 1, b"\xff"),
    (ctypes.c_uint16, 2**16 - 1, b"\xff\xff"),
    (ctypes.c_uint32, 2**32 - 1, b"\xff\xff\xff\xff"),
    (ctypes.c_uint64, 2**64 - 1, b"\xff\xff\xff\xff\xff\xff\xff\xff"),
    (int, 1, b"\x00\x00\x00\x01\x01"),
    (int, -1, b"\x00\x00\x00\x01\xff"),
    (int, -255, b"\x00\x00\x00\x02\xff\x01"),
    (int, -256, b"\x00\x00\x00\x02\xff\x00"),
    (int, 0, b"\x00\x00\x00\x00"),
    (int, 0x9A378F9B2E332A7, bytes.fromhex("0000000809a378f9b2e332a7")),
    (int, 0x80, b"\x00\x00\x00\x02\x00\x80"),
    (int, -0x1234, bytes.fromhex("00000002edcc")),
    (int, 2**32 - 1, b"\x00\x00\x00\x05\x00\xff\xff\xff\xff"),
    (bytes, b"hello", b"\x00\x00\x00\x05hello"),
    (str, "hello", b"\x00\x00\x00\x05hello"),
    (Rest, Rest(b"restdata"), b"restdata"),  # type: ignore[type-arg
]


@pytest.mark.parametrize("ctype,value,want", testdata_writer)
def test_streamwriter(ctype: type, value: Any, want: bytes) -> None:
    writer = StreamWriter()
    writer.write(ctype, value)
    got = writer.get_bytes()
    assert got == want


testdata_reader: list[tuple[type, bytes, Any]] = [(ctype, want, value) for ctype, value, want in testdata_writer]


@pytest.mark.parametrize("ctype,value,want", testdata_reader)
def test_streamreader(ctype: type, value: bytes, want: Any) -> None:
    reader = StreamReader(value)
    got = reader.read(ctype)
    assert got == want
    assert reader.eof()


def test_streamreader_eof() -> None:
    reader = StreamReader(b"\x00\x01")
    assert not reader.eof()
    assert reader.read(ctypes.c_uint16) == 1
    assert reader.eof()
    with pytest.raises(EOFError):
        reader.read(ctypes.c_uint8)


def test_streamwriter_invalid_type():
    writer = StreamWriter()
    with pytest.raises(TypeError):
        writer.write(float, 1.0)  # pyright: ignore[reportCallIssue, reportArgumentType]


def test_streamreader_invalid_type():
    reader = StreamReader(b"\x00\x01")
    with pytest.raises(TypeError):
        reader.read(float)  # pyright: ignore[reportArgumentType]


def test_streamreader_rest():
    reader = StreamReader(b"\x00\x01restdata")
    got = reader.read(ctypes.c_uint16)
    assert got == 1
    got = reader.read(Rest)  # type: ignore[type-arg]
    assert got == Rest(b"restdata")  # type: ignore[type-arg]
    assert reader.eof()
