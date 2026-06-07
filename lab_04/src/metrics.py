import math
from pathlib import Path

from .robot_state import RobotState, MotionCommand


def compute_state_length(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def state_metrics(trajectory: list[RobotState]) -> dict:
    path_length = 0
    prev_state = trajectory[0]
    for state in trajectory[1:]:
        path_length += compute_state_length(prev_state.x, prev_state.y, state.x, state.y)
        prev_state = state
    final_state = trajectory[-1]
    return {
        'number_of_states': len(trajectory),
        'path_length': path_length,
        'final_x': final_state.x,
        'final_y': final_state.y,
        'final_theta': final_state.theta,
    }


def kinematic_metrics(commands: list[MotionCommand]) -> dict:
    min_command_speed = math.inf
    max_command_speed = -math.inf
    for command in commands:
        if command.v < min_command_speed:
            min_command_speed = command.v
        if command.v > max_command_speed:
            max_command_speed = command.v 
    return {
        'min_command_speed': min_command_speed,
        'max_command_speed': max_command_speed
    }


def compute_metrics(trajectory: list[RobotState], commands: list[MotionCommand]) -> dict:
    return {
        **state_metrics(trajectory),
        **kinematic_metrics(commands)
    }


def save_summary(metrics: dict, output_path: str | Path) -> None:
    with open(output_path, 'w', encoding='utf-8') as file:
        for key, value in metrics.items():
            file.write(f"{key}: {value}\n")