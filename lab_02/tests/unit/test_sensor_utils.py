import pytest
from src.sensor_utils import generate_sensor_reading


@pytest.mark.parametrize('distance_cm, noise_range', [
    (100.0, 5.0),
    (0.0,   0.0),
    (50.0,  10.0),
])
def test_generate_sensor_reading_returns_float(distance_cm, noise_range):
    result = generate_sensor_reading(distance_cm, noise_range)
    assert isinstance(result, float)

@pytest.mark.parametrize('distance_cm, noise_range', [
    (100.0, 5.0),
    (50.0,  10.0),
    (20.0,  0.0),
])
def test_generate_sensor_reading_within_range(distance_cm, noise_range):
    result = generate_sensor_reading(distance_cm, noise_range)
    assert distance_cm - noise_range <= result <= distance_cm + noise_range

@pytest.mark.parametrize('distance_cm, noise_range', [
    (-1.0,  5.0),
    (100.0, -1.0),
])
def test_generate_sensor_reading_invalid_params(distance_cm, noise_range):
    with pytest.raises(ValueError):
        generate_sensor_reading(distance_cm, noise_range)
