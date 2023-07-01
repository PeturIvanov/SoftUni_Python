from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f"[{', '.join(reversed([el for el in self.data]))}]"
