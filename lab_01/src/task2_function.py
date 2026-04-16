import math

def math_func(x: int | float) -> float:
    eps = 1e-7
    return 2 * x ** 2 + math.log(x + eps) ** 2 + math.sin(x)