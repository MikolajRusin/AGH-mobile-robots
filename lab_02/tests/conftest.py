import pytest
from src.serial_utils import SerialPortFixture


@pytest.fixture
def serial_port() -> SerialPortFixture:
    return SerialPortFixture()
