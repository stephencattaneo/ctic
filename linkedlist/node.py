from typing import Any

class Node:
    data = None
    next = None

    def __init__(self, data: Any) -> None:
        self.data = data

class DoubleNode(Node):
    previous = None

    def __init__(self, data: Any, previous: Any = None) -> None:
        super().__init__(data)
        self.previous = previous
