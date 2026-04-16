from collections import deque

class FilterFIR:
    def __init__(self, filter_length: int):
        self.reservoir = deque(maxlen=filter_length)

    def filter(self, value: float) -> float:
        self.reservoir.append(value)
        return sum(self.reservoir) / len(self.reservoir)