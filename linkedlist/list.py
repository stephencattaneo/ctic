from typing import Any

from .node import Node, DoubleNode


class List:
    head = None

    def __init__(self, args: list = None ) -> None:
        if args:
            for i in args:
                self.append(i)

    def append(self, data: Any) -> None:
        if not self.head:
            self.head = Node(data)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def __len__(self):
        count = 0
        curr = self.head

        while curr:
            curr = curr.next
            count += 1

        return count

    def delete(self, value: Any) -> bool:
        if not self.head:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                return True
            
            prev = curr
            curr = curr.next

        return False


class DoubleList(List):
    tail = None

    def append(self, data: Any) -> None:
        if not self.head:
            self.head = self.tail = DoubleNode(data)
        else:
            prevtail = self.tail
            self.tail = DoubleNode(data, self.tail)
            prevtail.next = self.tail

    def delete(self, value: Any) -> bool:
        if not self.head:
            return False

        if self.head.data == value:
            self.head = self.head.next
            self.head.previous = None
            return True

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                curr.next.previous = prev
                return True
            
            prev = curr
            curr = curr.next

        return False
