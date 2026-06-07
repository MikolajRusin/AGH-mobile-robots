import pytest
from src.serial_utils import SerialPortFixture, SerialPortWrite, SerialPortRead


@pytest.mark.parametrize('message, expected', [
    ('A',    b'A'),
    ('Test', b'Test'),
])
def test_serial_write_encodes_to_bytes(serial_port, message, expected):
    SerialPortWrite(serial_port, message)
    assert serial_port.serial_port_values == expected

def test_serial_multiple_writes_append(serial_port):
    SerialPortWrite(serial_port, 'Hello')
    SerialPortWrite(serial_port, 'World')
    assert serial_port.serial_port_values == b'HelloWorld'

def test_serial_write_then_read(serial_port):
    SerialPortWrite(serial_port, 'Python')
    assert SerialPortRead(serial_port) == b'Python'

def test_serial_read_clears_buffer(serial_port):
    SerialPortWrite(serial_port, 'data')
    SerialPortRead(serial_port)
    assert serial_port.serial_port_values == b''

def test_serial_read_empty_buffer(serial_port):
    assert SerialPortRead(serial_port) == b''
