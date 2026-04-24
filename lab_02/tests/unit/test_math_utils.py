import math
import pytest
from src.math_utils import calculate_expression


def _expected(x: float) -> float:
    return 2 * x**2 + math.log(x)**2 + math.sin(x)

@pytest.mark.parametrize('value, expected', [
    (0.002, _expected(0.002)),
    (1,     _expected(1)),
    (2.0,   _expected(2.0)),
    (100,   _expected(100)),
])
def test_calculate_expression(value, expected):
    assert calculate_expression(value) == pytest.approx(expected)

@pytest.mark.parametrize('value', [0, -1, -0.5])
def test_calculate_expression_invalid(value):
    with pytest.raises(ValueError):
        calculate_expression(value)
