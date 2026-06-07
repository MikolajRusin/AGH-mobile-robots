from pathlib import Path

from src.robot_state import RobotState
from src.serial_utils import SerialPortFixture, SerialPortWrite
from src.experiment_runner import run_experiment_from_serial


OUTPUT_DIR = Path(__file__).parent / 'results'
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)

commands_text = """
0.10,0.10,1.0
0.25,0.25,1.0
0.45,0.45,1.0
0.20,0.50,2.0
0.50,0.20,2.0
0.30,0.30,1.0
0.10,0.10,1.0
"""

def run_experiment():
    serial_port = SerialPortFixture()
    SerialPortWrite(serial_port, commands_text + "\n")
    summary = run_experiment_from_serial(
        serial_port=serial_port,
        initial_state=RobotState(0.0, 0.0, 0.0),
        wheel_base=0.5,
        dt=0.05,
        output_dir=OUTPUT_DIR,
    )
    return summary


run_experiment()