from pathlib import Path

from .robot_state import RobotState
from .serial_utils import SerialPortFixture, SerialPortRead
from .command_parser import commands_from_text
from .simulator import simulate_commands, save_trajectory_csv, plot_trajectory
from .metrics import compute_metrics, save_summary


def run_experiment_from_serial(
    serial_port: SerialPortFixture,
    initial_state: RobotState,
    wheel_base: float,
    dt: float,
    output_dir: str,
) -> dict[str, float]:
    read_text = SerialPortRead(serial_port)
    read_text = read_text.decode()
    commands_list = commands_from_text(read_text, wheel_base)
    trajectory = simulate_commands(initial_state, commands_list, dt)
    metrics = compute_metrics(trajectory, commands_list)
    save_trajectory_csv(trajectory, Path(output_dir) / 'trajectory.csv')
    plot_trajectory(trajectory, Path(output_dir) / 'trajectory.png')
    save_summary(metrics, Path(output_dir) / 'summary.txt')
    return metrics