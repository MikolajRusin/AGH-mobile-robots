import csv
from pathlib import Path
import matplotlib.pyplot as plt
from .robot_state import RobotState, MotionCommand
from .kinematics import update_robot_state, wheel_speeds_to_velocity

def simulate_commands(state: RobotState, motion_commands: list[MotionCommand], dt: float) -> list[RobotState]:
    trajectory = [state]
    for command in motion_commands:
        steps = int(command.duration // dt)
        last_dt = command.duration % dt
        for _ in range(steps):
            state = update_robot_state(state, v=command.v, omega=command.omega, dt=dt)
            trajectory.append(state)
        if last_dt > 1e-9:
            state = update_robot_state(state, v=command.v, omega=command.omega, dt=last_dt)
            trajectory.append(state)

    return trajectory

def save_trajectory_csv(trajectory: list[RobotState], output_path: str | Path) -> None:
    data = [[state.x, state.y] for state in trajectory]
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def plot_trajectory(trajectory: list[RobotState], output_path: str | Path) -> None:
    x = [state.x  for state in trajectory]
    y = [state.y for state in trajectory]

    plt.plot(x, y, marker='.', markersize=3)
    plt.scatter(x[0], y[0], label='start', marker='.', c='b', s=100)
    plt.scatter(x[-1], y[-1], label='start', marker='x', c='r', s=100)
    plt.legend()
    plt.savefig(output_path)
