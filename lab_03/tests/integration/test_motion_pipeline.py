import pytest
from src.kinematics import update_robot_state, wheel_speeds_to_velocity
from src.robot_state import RobotState, MotionCommand
from src.simulator import simulate_commands


def test_full_motion_pipeline_from_wheel_speeds_to_trajectory():
    wheel_base = 0.5
    v_left = 0.3
    v_right = 0.5
    v, omega = wheel_speeds_to_velocity(v_left, v_right, wheel_base)
    commands = [MotionCommand(v=v, omega=omega, duration=1.0)]
    trajectory = simulate_commands(RobotState(0.0, 0.0, 0.0), commands, dt=0.1)

    assert len(trajectory) > 1
    assert trajectory[-1].x > 0.0
    assert trajectory[-1].theta == pytest.approx(omega * 1.0)