import pytest
import math
from src.kinematics import update_robot_state, wheel_speeds_to_velocity
from src.robot_state import RobotState

@pytest.mark.parametrize('v, omega, dt, x_expected, y_expected, theta_expected', [
    (1.0, 0.0, 1.0, 1.0, 0.0, 0.0),
    (1.0, 0.0, 0.5, 0.5, 0.0, 0.0)
])
def test_robot_moves_straight(v, omega, dt, x_expected, y_expected, theta_expected):
    state = RobotState(x=0.0, y=0.0, theta=0.0)
    new_state = update_robot_state(state, v=v, omega=omega, dt=dt)

    assert new_state.x == pytest.approx(x_expected)
    assert new_state.y == pytest.approx(y_expected)
    assert new_state.theta == pytest.approx(theta_expected)

@pytest.mark.parametrize('v, omega, dt, x_expected, y_expected, theta_expected', [
    (1.0, 0.0, 1.0, 0.0, 1.0, math.pi / 2),
    (1.0, 0.0, 0.5, 0.0, 0.5, math.pi / 2)
])
def test_robot_moves_y_axis(v, omega, dt, x_expected, y_expected, theta_expected):
    state = RobotState(x=0.0, y=0.0, theta=math.pi / 2)
    new_state = update_robot_state(state, v=v, omega=omega, dt=dt)

    assert new_state.x == pytest.approx(x_expected)
    assert new_state.y == pytest.approx(y_expected)
    assert new_state.theta == pytest.approx(theta_expected)

@pytest.mark.parametrize('v, omega, dt, x_expected, y_expected, theta_expected', [
    (0.0, 1.0, 1.0, 0.0, 0.0, 1.0),
    (0.0, -math.pi / 2, 1.0, 0.0, 0.0, -math.pi / 2)
])
def test_robot_turn_in_place(v, omega, dt, x_expected, y_expected, theta_expected):
    state = RobotState(x=0.0, y=0.0, theta=0.0)
    new_state = update_robot_state(state, v=v, omega=omega, dt=dt)

    assert new_state.x == pytest.approx(x_expected)
    assert new_state.y == pytest.approx(y_expected)
    assert new_state.theta == pytest.approx(theta_expected)

@pytest.mark.parametrize('dt', [
    0.0, -0.2
])
def test_robot_invalid_dt(dt):
    state = RobotState(x=0.0, y=0.0, theta=0.0)
    with pytest.raises(ValueError):
        new_state = update_robot_state(state, v=1.0, omega=0.0, dt=dt)

@pytest.mark.parametrize('wheel_base', [
    0.0, -10.0
])
def test_robot_invalid_wheel_base(wheel_base):
    state = RobotState(x=0.0, y=0.0, theta=0.0)
    with pytest.raises(ValueError):
        new_state = wheel_speeds_to_velocity(v_left=1.0, v_right=10.0, wheel_base=wheel_base)