from typing import Any

class Node:
    data = None
    next = None

    def __init__(self, data: Any, next: Any = None) -> None:
        self.data = data
        self.next = next

class DoubleNode(Node):
    previous = None

    def __init__(self, data: Any, previous: Any = None) -> None:
        super().__init__(data)
        self.previous = previous
