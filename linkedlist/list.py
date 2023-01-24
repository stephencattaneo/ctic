from typing import Any

from .node import Node, DoubleNode


class List:
    head = None

    def append(self, data: Any) -> None:
        if not self.head:
            self.head = Node(data)

        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

class DoubleList:
    head = None
    tail = None

    def append(self, data: Any) -> None:
        if not self.head:
            self.head = self.tail = DoubleNode(data)
        else:
            prevtail = self.tail
            self.tail = DoubleNode(data, self.tail)
            prevtail.next = self.tail
