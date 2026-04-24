import math

def calculate_expression(x: float) -> float:
    if x <= 0:
        raise ValueError('Argument x has to be higher than 0.')
    return 2 * x**2 + math.log(x)**2 + math.sin(x)