def moving_average(data: list[float], window_size: int) -> list[float]:
    if window_size <= 0:
        raise ValueError('Rozmiar okna musi być dodatni.')
    if window_size > len(data):
        raise ValueError('Rozmiar okna nie może być większy od liczby próbek.')
    return [sum(data[i:i + window_size]) / window_size for i in range(len(data) - window_size + 1)]
