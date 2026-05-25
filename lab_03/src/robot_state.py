from dataclasses import dataclass


@dataclass(frozen=True)
class RobotState:
    x: float
    y: float
    theta: float

@dataclass(frozen=True)
class MotionCommand:
    v: float
    omega: float
    duration: float