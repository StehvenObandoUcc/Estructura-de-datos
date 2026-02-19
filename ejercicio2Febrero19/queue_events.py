from collections import deque


class Event:
    def __init__(self, name: str, description: str, energy: int, heart_rate: int, temperature: int):
        self.name        = name
        self.description = description
        self.energy      = energy
        self.heart_rate  = heart_rate
        self.temperature = temperature

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class EventQueue:
    def __init__(self, events: list):
        self._queue = deque(events)

    def next(self):
        return self._queue.popleft() if self._queue else None

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def remaining(self) -> int:
        return len(self._queue)
