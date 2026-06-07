from src.robot_state import RobotState
from src.serial_utils import SerialPortWrite
from src.experiment_runner import run_experiment_from_serial


def test_serial_to_simulator_pipeline(serial_port, tmp_path):
    commands_text = """
0.10,0.10,1.0
0.25,0.25,1.0
0.20,0.50,2.0
0.30,0.30,1.0
"""

    SerialPortWrite(serial_port, commands_text.strip() + "\n")

    summary = run_experiment_from_serial(
        serial_port=serial_port,
        initial_state=RobotState(0.0, 0.0, 0.0),
        wheel_base=0.5,
        dt=0.05,
        output_dir=tmp_path,
    )

    assert (tmp_path / 'trajectory.csv').exists()
    assert (tmp_path / 'trajectory.png').exists()
    assert (tmp_path / 'summary.txt').exists()

    assert summary['path_length'] > 0
    assert summary['final_theta'] != 0.0