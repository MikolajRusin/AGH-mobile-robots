import pytest
from src.serial_utils import SerialPortFixture, SerialPortWrite, SerialPortRead
from src.sensor_utils import generate_sensor_reading
from src.filter_utils import moving_average


def test_serial_type_conversion(serial_port):
    '''bytes -> str -> float nie rzuca wyjątku i zachowuje wartość.'''
    original = 123.45

    SerialPortWrite(serial_port, str(original))
    raw = SerialPortRead(serial_port)

    assert isinstance(raw, bytes)
    decoded = float(raw.decode())
    assert decoded == pytest.approx(original)


def test_sensor_pipeline(serial_port):
    '''
    Pełny pipeline:
      generate_sensor_reading
        -> SerialPortWrite (float -> str -> bytes)
        -> SerialPortRead  (bytes -> str -> float)
        -> moving_average
    '''
    distance_cm = 100.0
    noise_range = 5.0
    n_samples = 6
    window_size = 3

    # 1. Generuj -> zapisz -> odczytaj -> dekoduj (każda próbka osobno)
    samples: list[float] = []
    for _ in range(n_samples):
        value = generate_sensor_reading(distance_cm, noise_range)
        SerialPortWrite(serial_port, str(value))

        raw = SerialPortRead(serial_port)
        assert isinstance(raw, bytes)

        decoded = float(raw.decode())
        assert isinstance(decoded, float)
        samples.append(decoded)

    # 2. Każda próbka mieści się w oczekiwanym zakresie
    for s in samples:
        assert distance_cm - noise_range <= s <= distance_cm + noise_range

    # 3. Filtracja
    filtered = moving_average(samples, window_size)

    # 4. Liczba wyników zgodna z wzorem: n - window + 1
    assert len(filtered) == n_samples - window_size + 1

    # 5. Wyniki po filtracji nadal w dopuszczalnym zakresie
    for val in filtered:
        assert distance_cm - noise_range <= val <= distance_cm + noise_range
