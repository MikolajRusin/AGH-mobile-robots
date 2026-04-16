import sys
import serial

from src.task2_function import math_func
from src.serial_comm import open_serial_port, create_ports, kill_ports
from src.task5_filter import FilterFIR

PORT = '/dev/pts/5'
BAUDRATE = 115200
TIMEOUT = 6


def task_1():
    print('=== Task 1 ===')
    print(f'Hello {sys.version}')
    print('\n')


def task_2():
    print('=== Task 2 ===')
    x = 0.31
    func_result = math_func(x)
    print(f'f(x={x}) = {func_result}')
    print('\n')


def task_3():
    print('=== Task 3 ===')
    open_serial_port(PORT, timeout=TIMEOUT)
    print('\n')


def task_4():
    print('=== Task 4 ===')
    try:
        p1, p2, socat = create_ports()
        print(f'Created ports: {p1}, {p2}')

        ser = serial.Serial(p1, baudrate=BAUDRATE, timeout=TIMEOUT)
        while True:
            response = ser.readline()
            if not response:
                break

            device_distance = float(response.decode())
            print(device_distance)
    finally:
        ser.close()
        kill_ports()
    print('\n')


def task_5():
    print('=== Task 5 ===')
    try:
        p1, p2, socat = create_ports()
        print(f'Created ports: {p1}, {p2}')

        ser = serial.Serial(p1, baudrate=BAUDRATE, timeout=TIMEOUT)
        FIR = FilterFIR(filter_length=10)
        while True:
            response = ser.readline()
            if not response:
                break

            device_distance = float(response.decode())
            device_distance = FIR.filter(device_distance)
            print(device_distance)
    finally:
        ser.close()
        kill_ports()
    print('\n')

TASKS = {
    '1': task_1,
    '2': task_2,
    '3': task_3,
    '4': task_4,
    '5': task_5,
}

if __name__ == '__main__':
    task = input('Type the number of the task: ')
    if task not in TASKS:
        print(f'Unknown task: {task}')
        sys.exit(1)

    TASKS[task]()
