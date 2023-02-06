from typing import Any

class Node:
    data = None
    next = None

    def __init__(self, data) -> None:
        self.data = data

class Queue:
    head = None
    tail = None

    def __init__(self, items = None) -> None:
        if items:
            for item in items:
                self.add(item)

    def add(self, item: Any) -> None:
        item = Node(item)
        if not self.head:
            self.head = self.tail = item
        else:
            self.tail.next = item
            self.tail = self.tail.next

    def remove(self) -> Any:
        if not self.head:
            raise Exception('empty list')

        value = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return value

    def peek(self) -> Any:
        if not self.head:
            raise Exception('empty list')

        return self.head.data

    def is_empty(self) -> bool:
        return not self.head

class ArrayQueue:
    def __init__(self) -> None:
        self.storage = []
        self.head = None
        self.tail = None

    def add(self, item: int) -> None:
        storage_size = len(self.storage)
        if self.head is None:
            self.head = self.tail = 0
            if storage_size < 1:
                self.storage.append(item)
            else:
                self.storage[self.head] = item
            return


        queue_tail = self.tail if self.tail >= self.head else self.tail + storage_size
        queue_size = queue_tail - self.head + 1
        if (queue_size + 1) > storage_size:
            '''
              insert index into array, growing it.
            '''
            new_index = self.tail + 1
            self.storage.insert(new_index, item)
            self.tail = new_index
            if self.tail <= self.head:
                self.head += 1
        else:
            '''
              re-use existing array index.
            '''
            new_index = (self.tail + 1) % storage_size
            self.storage[new_index] = item
            self.tail = new_index

    def remove(self) -> int:
        if self.head is None:
            raise Exception('Empty Queue')

        value = self.storage[self.head]

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            storage_size = len(self.storage)
            self.head = (self.head + 1) % storage_size

        return value

    def peek(self) -> int:
        if self.head is None:
            raise Exception('Empty Queue')

        return self.storage[self.head]

    def is_empty(self) -> bool:
        return self.head is None
