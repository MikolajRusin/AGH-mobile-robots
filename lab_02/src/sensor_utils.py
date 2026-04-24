import random


def generate_sensor_reading(distance_cm: float, noise_range: float) -> float:
    if distance_cm < 0:
        raise ValueError('distance_cm must be non-negative.')
    if noise_range < 0:
        raise ValueError('noise_range must be non-negative.')
    return distance_cm + random.uniform(-noise_range, noise_range)
