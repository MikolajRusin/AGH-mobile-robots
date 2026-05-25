import math
from .robot_state import RobotState

def update_robot_state(state: RobotState, v: float, omega: float, dt: float) -> RobotState:
    if dt <= 0:
        raise ValueError('The time step dt must be greater than 0.')

    x_new = state.x + v * math.cos(state.theta) * dt
    y_new = state.y + v * math.sin(state.theta) * dt
    theta_new = state.theta + omega * dt
    return RobotState(x_new, y_new, theta_new)

def wheel_speeds_to_velocity(v_left: float, v_right: float, wheel_base: float) -> tuple[float, float]:
    if wheel_base <= 0:
        raise ValueError('The wheelbase must be greater than 0.')

    v = (v_right + v_left) / 2.0
    omega = (v_right - v_left) / wheel_base
    return (v, omega)