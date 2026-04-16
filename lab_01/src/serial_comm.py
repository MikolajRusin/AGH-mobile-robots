import serial
import subprocess
from pathlib import Path


SCRIPTS_DIR = Path(__file__).parents[1] / 'scripts'


def create_ports():
    socat = subprocess.Popen(
        ['bash', str(SCRIPTS_DIR / 'create-ports.sh')],
        stderr=subprocess.PIPE,
        text=True
    )

    ports = []
    while len(ports) < 2:
        line = socat.stderr.readline()
        port_name = line.strip().split(' ')[-1]
        ports.append(port_name)

    return ports[0], ports[1], socat


def kill_ports():
    subprocess.run(
        ['bash', str(SCRIPTS_DIR / 'kill-ports.sh')]
    )


def open_serial_port(port: str, baudrate: int = 115200, timeout: int = 2):
    ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
    print(f'Opened port: {ser.name}')

    ser.write(b'Hello from receiver\n')

    response = ser.readline()
    print(f'Received: {response.decode().strip()}')

    ser.close()
    print('Port closed')
