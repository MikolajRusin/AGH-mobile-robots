from serial import Serial


class SerialPortFixture(Serial):
    def __init__(self):
        self.serial_port_values: bytes = b''

    def write(self, data: bytes) -> None:
        self.serial_port_values += data

    def read(self, size: int = -1) -> bytes:
        if size == -1:
            data = self.serial_port_values
            self.serial_port_values = b''
            return data
        data = self.serial_port_values[:size]
        self.serial_port_values = self.serial_port_values[size:]
        return data


def SerialPortWrite(port: SerialPortFixture, message: str) -> None:
    port.write(message.encode())


def SerialPortRead(port: SerialPortFixture) -> bytes:
    return port.read()