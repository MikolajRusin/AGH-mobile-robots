from pathlib import Path
from src.robot_state import MotionCommand, RobotState
from src.simulator import simulate_commands, save_trajectory_csv, plot_trajectory

LAB_PATH = Path(__file__).parent
RESULTS_PATH = LAB_PATH / 'results'
RESULTS_PATH.mkdir(parents=True, exist_ok=True)

if __name__ == '__main__':
    commands = [
        MotionCommand(v=0.50, omega=0.00, duration=2.0),
        MotionCommand(v=0.35, omega=0.60, duration=4.0),
        MotionCommand(v=0.35, omega=-0.60, duration=4.0),
        MotionCommand(v=0.00, omega=1.00, duration=1.5),
        MotionCommand(v=0.45, omega=-0.40, duration=3.0)
    ]
    initial_state = RobotState(0.0, 0.0, 0.0)
    comm = simulate_commands(initial_state, commands, dt=0.05)
    save_trajectory_csv(comm, RESULTS_PATH / 'trajectory.csv')
    plot_trajectory(comm, RESULTS_PATH / 'trajectory.png')