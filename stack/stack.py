class Node:
    data = None
    next = None

    def __init__(self, data: int, next=None):
        self.data = data
        self.next = next

class Stack:
    top = None

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, data: int):
        self.top = Node(data, self.top)

    def pop(self):
        try:
            return_value = self.top.data
            self.top = self.top.next
            return return_value
        except AttributeError:
           raise Exception('Empty Stack')

    def peek(self):
        try:
            return self.top.data
        except AttributeError:
           raise Exception('Empty Stack')