from src.robot_state import RobotState, MotionCommand
from src.simulator import simulate_commands


def test_trajectory_starts_with_initial_state():
    initial = RobotState(1.0, 2.0, 0.5)
    commands = [MotionCommand(v=1.0, omega=0.0, duration=1.0)]
    trajectory = simulate_commands(initial, commands, dt=0.1)

    assert trajectory[0] == initial


def test_trajectory_length_matches_steps():
    initial = RobotState(0.0, 0.0, 0.0)
    commands = [MotionCommand(v=1.0, omega=0.0, duration=1.0)]
    trajectory = simulate_commands(initial, commands, dt=0.1)

    assert len(trajectory) == 11


def test_empty_commands_returns_only_initial_state():
    initial = RobotState(0.0, 0.0, 0.0)
    trajectory = simulate_commands(initial, [], dt=0.1)

    assert len(trajectory) == 1
    assert trajectory[0] == initial
