# Lab 01 — Introduction to Python

## Table of Contents

- [Running](#running)
- [File Structure](#file-structure)
- [Tasks](#tasks)
  - [Task 1 — Environment Setup](#task-1--environment-setup)
  - [Task 2 — Mathematical Function](#task-2--mathematical-function)
  - [Task 3 — Serial Communication](#task-3--serial-communication)
  - [Task 4 — Sensor Data Reading](#task-4--sensor-data-reading)
  - [Task 5 — Noise Filtering](#task-5--noise-filtering)
- [Dependencies](#dependencies)

---

## Running

```bash
# Install dependencies
uv sync

# Run a task
python main.py
# Enter task number: 1 / 2 / 3 / 4 / 5
```

---

## File Structure

```
lab_01/
├── main.py                     # Entry point — task selection
├── scripts/
│   ├── create-ports.sh         # Creates a virtual serial port pair (socat)
│   ├── kill-ports.sh           # Kills socat processes
│   └── run-miniterm.sh         # Launches serial terminal
├── src/
│   ├── task2_function.py       # Mathematical function (Task 2)
│   ├── serial_comm.py          # Serial port handling (Tasks 3, 4)
│   └── task5_filter.py         # FIR filter (Task 5)
└── report/
```

---

## Tasks

### Task 1 — Environment Setup

Verifies the Python version.

### Task 2 — Mathematical Function

Implementation of the function:

$$y = 2x^2 + \log(x)^2 + \sin(x)$$

| File | Function |
|------|----------|
| `src/task2_function.py` | `math_func(x)` |

### Task 3 — Serial Communication

Connects to a serial port, sends a message and receives a response.

**Environment setup (Linux):**

```bash
# Terminal 1 — create virtual port pair
./scripts/create-ports.sh
# e.g. /dev/pts/5 and /dev/pts/6

# Terminal 2 — launch serial terminal on the second port
./scripts/run-miniterm.sh --port_number 6
```

Set the `PORT` variable in `main.py` to the first port (e.g. `/dev/pts/5`).

| File | Function |
|------|----------|
| `src/serial_comm.py` | `open_serial_port(port, baudrate, timeout)` |

### Task 4 — Sensor Data Reading

Receives data from a distance sensor simulator (values in cm with measurement noise) over a serial port.

**Running the simulator:**

```bash
# Separate terminal — simulator sends data to the second port of the pair
python distance_sensor_simulator.py --port_number 6
```

Task 4 creates the port pair automatically via `create_ports()`.

| File | Description |
|------|-------------|
| `src/serial_comm.py` | `create_ports()`, `kill_ports()` |
| `scripts/distance_sensor_simulator.py` | Distance sensor simulator |

### Task 5 — Noise Filtering

Sensor data is processed by a FIR filter (moving average) to reduce measurement noise.

| Parameter | Value |
|-----------|-------|
| Filter type | FIR (moving average) |
| Filter length | 10 samples |

| File | Class |
|------|-------|
| `src/task5_filter.py` | `FilterFIR(filter_length)` |

---

## Dependencies

| Library | Usage |
|---------|-------|
| `pyserial` | Serial port communication |

**System requirements:** `socat` (Linux) or `com0com` (Windows) for virtual serial ports.
