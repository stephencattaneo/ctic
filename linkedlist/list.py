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
        return curr.next

    def prepend(self, data: Any) -> None:
        self.head = Node(data, next=self.head)

    def __len__(self) -> int:
        count = 0
        curr = self.head

        while curr:
            curr = curr.next
            count += 1

        return count

    def len_and_tail(self) -> list:
        count = 0
        curr = self.head
        last = None

        while curr:
            last = curr
            curr = curr.next
            count += 1

        return count, last

    def __iter__(self): #XXX python3.9 return custom class
        self.iter_cursor = self.head
        return self

    def __next__(self) -> Any:
        if not self.iter_cursor:
            raise StopIteration

        value = self.iter_cursor.data
        self.iter_cursor = self.iter_cursor.next

        return value


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

    def dedupe(self) -> None:
        if not self.head:
            return

        values = {self.head.data: True}

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data in values:
                curr = prev.next = curr.next
            else:
                values[curr.data] = True
                prev = curr
                curr = curr.next

    def kth_to_last(self, nth: int) -> Any:
        target = len(self) - nth + 1

        if target < 1:
            return None

        count = 1
        curr = self.head

        while count < target:
            curr = curr.next
            count += 1

        return curr.data

    def partition_by_value(self, partition: int) -> Any:
        curr = self.head
        before = List()
        after = List()

        while curr:
            if curr.data < partition:
                before.append(curr.data)
            else:
                after.append(curr.data)
            curr = curr.next

        return before, after

    def sum(self, other: Any) -> Any:
        self_len = len(self)
        other_len = len(other)

        self_curr = self.head
        other_curr = other.head

        # 1. need to ensure lists are the same length which may require padding.
        # 2. do not mutate self or other

        if self_len < other_len:
            self_curr = self.__pad_list(self_curr, other_len - self_len)
        elif other_len < self_len:
            other_curr = self.__pad_list(other_curr, self_len - other_len)

        summed_list = List()
        lower_digits = self.__sum_helper(self_curr, other_curr)

        if lower_digits["carry"]:
            summed_list.head = Node(lower_digits["carry"])
            summed_list.head.next = lower_digits["node"]
        else:
            summed_list.head = lower_digits["node"]

        return summed_list

    def __pad_list(self, l1: Any, count: int) -> Any:
        l2_head = None
        curr = None

        while count > 0:
            if not l2_head:
                l2_head = curr = Node(0)
            else:
                curr.next = Node(0)
                curr = curr.next
            count -= 1

        while l1:
            curr.next = Node(l1.data)
            curr = curr.next
            l1 = l1.next

        return l2_head

    def __sum_helper(self, l1, l2) -> dict:
        if not l1: # assume even sized lists
            return {
                "node": None,
                "carry": 0
            }

        prevDigit = self.__sum_helper(l1.next, l2.next)
        total = l1.data + l2.data + prevDigit["carry"]
        node = Node(total % 10)
        node.next = prevDigit["node"]

        return {
            "node": node,
            "carry": total // 10
        }

    def reverse_order_sum(self, other: Any) -> Any:
        carry_over = 0
        out = List()
        self_cur = self.head
        other_cur = other.head

        while self_cur or other_cur or carry_over:
            total = getattr(self_cur, 'data', 0) + getattr(other_cur, 'data', 0) + carry_over
            carry_over = total // 10
            out.append(total % 10)

            self_cur = getattr(self_cur, 'next', None)
            other_cur = getattr(other_cur, 'next', None)

        return out

    def is_palendrom(self):
        other = List()

        cur = self.head
        count = 0
        while cur:
            other.prepend(cur.data)
            cur = cur.next
            count += 1

        cur = self.head
        other_cur = other.head
        count = (count // 2) + (count % 2) # only need to compare 60% of the string
        while count > 0:
            if not cur.data == other_cur.data:
                return False
            cur = cur.next
            other_cur = other_cur.next
            count -= 1

        return True

    def __palendrom_helper(self, left, right):
        return left == right

    def does_intersect(self, other: Any) -> Any:
        # # !! this works but requires additional storage
        # cur = self.head
        # seen = {}
        # while cur:
        #     seen[cur] = True
        #     cur = cur.next

        # cur = other.head
        # while cur:
        #     if cur in seen:
        #         return cur
        #     cur = cur.next

        # return None

        # !! No additional storage required
        # count & compare tails
        self_count, self_tail = self.len_and_tail()
        other_count, other_tail = other.len_and_tail()

        if self_tail != other_tail:
            return None

        # move cursor of longer forward until same length
        self_curr = self.head
        other_curr = other.head
        diff = abs(self_count - other_count)
        if self_count > other_count:
            self_curr = self.node_at(diff)
        else:
            other_curr = other.node_at(diff)

        # compare until same node is found
        while self_curr and other_curr:
            if self_curr == other_curr:
                return self_curr

            self_curr = self_curr.next
            other_curr = other_curr.next

    def node_at(self, count: int) -> Any:
        curr = self.head
        while count > 0 and curr:
            count -= 1
            curr = curr.next

        return curr

    def find_loop(self) -> Any:
        '''
          TLDR - 2 cursors, move for 2nd cursor twice as fast.
          if there is a loop eventually cur1 and cur2 will be the samething.
          if not cur1 will reach the end
        '''
        cur1 = self.head
        cur2 = self.head

        while cur1 and cur2:
            cur1 = cur1.next
            cur2 = getattr(cur2, 'next', None)
            cur2 = getattr(cur2, 'next', None)
            if cur1 == cur2:
                break

        if not (cur1 and cur2):
            return None

        cur1 = self.head

        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        return cur2

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
