class Stack:
    def __init__(self):
        self._elements: list = []

    def push(self, element) -> None:
        self._elements.append(element)

    def pop(self):
        return self._elements.pop() if not self.is_empty() else None

    def peek(self):
        return self._elements[-1] if not self.is_empty() else None

    def is_empty(self) -> bool:
        return len(self._elements) == 0

    def size(self) -> int:
        return len(self._elements)

    def all_items(self) -> list:
        return list(reversed(self._elements))
