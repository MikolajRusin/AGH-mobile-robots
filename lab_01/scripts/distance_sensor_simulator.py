import serial
import random
import time
import argparse


TIMEOUT = 1

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port_number')

    args = parser.parse_args()
    return args

def run_device(port: str, baudrate: int = 115200, timeout: int = 2):
    ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
    print(f'Device is running...')

    try:
        max_distance = 25.0
        min_distance = 0.0
        distance = 25.0
        distance_dt = 0.1
        direction = 0
        while True:
            if distance < min_distance or distance > max_distance:
                direction = int(not direction) 

            noise = random.uniform(-0.05, 0.05)
            if direction:
                distance += distance_dt
            else:
                distance -= distance_dt
            
            sensor_read = distance + noise
            ser.write(f'{sensor_read}\n'.encode())
            time.sleep(0.5)

    finally:
        ser.close()
        print('Port closed')

if __name__ == '__main__':
    args = parse_args()
    port = f'/dev/pts/{args.port_number}'
    
    run_device(port, timeout=TIMEOUT)