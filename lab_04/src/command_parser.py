from .robot_state import MotionCommand
from .kinematics import wheel_speeds_to_velocity


def parse_wheel_command(line: str) -> tuple[float, float, float]:
    values = tuple(map(float, line.replace(' ', '').split(',')))
    if len(values) != 3:
        raise ValueError('Expected 3 comma-separated values')
    return values

def command_from_line(line: str, wheel_base: float) -> MotionCommand:
    v_left, v_right, duration = parse_wheel_command(line)
    velocity, omega = wheel_speeds_to_velocity(v_left, v_right, wheel_base)
    return MotionCommand(velocity, omega, duration)


def commands_from_text(text: str, wheel_base: float) -> list[MotionCommand]:
    commands = []
    for line in text.split('\n'):
        if line:
            command = command_from_line(line, wheel_base)
            commands.append(command)
    return commands