import pytest
from src.filter_utils import moving_average


@pytest.mark.parametrize('data, window_size, expected', [
    ([1.0, 2.0, 3.0, 4.0, 5.0], 3, [2.0, 3.0, 4.0]),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 2, [1.5, 2.5, 3.5, 4.5]),
    ([1.0, 2.0, 3.0, 4.0, 5.0], 5, [3.0]),
    ([4.0, 4.0, 4.0],           1, [4.0, 4.0, 4.0]),
])
def test_moving_average_known_input(data, window_size, expected):
    assert moving_average(data, window_size) == pytest.approx(expected)

@pytest.mark.parametrize('window_size', [0, -1, -10])
def test_moving_average_invalid_window_size(window_size):
    with pytest.raises(ValueError):
        moving_average([1.0, 2.0, 3.0], window_size)

def test_moving_average_window_larger_than_data():
    with pytest.raises(ValueError):
        moving_average([1.0, 2.0], window_size=5)

def test_moving_average_reduces_variance():
    noisy = [10.0, 15.0, 8.0, 20.0, 7.0, 18.0, 9.0, 16.0]
    filtered = moving_average(noisy, window_size=3)

    def variance(seq):
        mean = sum(seq) / len(seq)
        return sum((x - mean) ** 2 for x in seq) / len(seq)

    assert variance(filtered) < variance(noisy)
