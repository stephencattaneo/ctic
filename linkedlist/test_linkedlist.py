from .list import List, DoubleList


class TestSingleLink:
    def test_emptylist_append(self):
        lut = List()
        assert lut.head is None

        lut.append(5)
        assert lut.head.data == 5
        assert lut.head.next is None

    def test_append_multiple_items(self):
        lut = List()

        lut.append(6)
        lut.append(3)

        assert lut.head.data == 6
        assert lut.head.next.data == 3

    def test_init_append(self):
        lut = List(range(5))

        assert lut.head.data == 0
        assert lut.head.next.data == 1

    def test_len(self):
        lut = List(range(2))

        assert len(lut) == 2

    def test_len_empty(self):
        assert len(List()) == 0

    def test_delete(self):
        lut = List(range(3))

        lut.delete(1)

        assert lut.head.next.data == 2

    def test_cast_to_list(self):
        lut = List(range(3))

        assert list(lut) == [0,1,2]


    def test_dedupe(self):
        lut = List(list(range(3)) + list(range(3)))
        lut.dedupe()

        assert list(lut) == [0, 1, 2]

    def test_kth_to_last(self):
        lut = List(range(4))

        assert lut.kth_to_last(1) == 3
        assert lut.kth_to_last(2) == 2

    def test_partition_by_value(self):
        lut = List([3, 5, 8, 5, 10, 2 , 1])
        part1, part2 = lut.partition_by_value(5)

        assert list(part1) == [3, 2, 1]
        assert list(part2) == [5, 8, 5, 10]

class TestDoubleLink:
    def test_empty_append(self):
        lut = DoubleList()
        assert lut.head is None
        assert lut.tail is None

        lut.append(9)
        assert lut.head == lut.tail
        assert lut.head.data == 9

    def test_append_multiple_items(self):
        lut = DoubleList()

        lut.append(342)
        lut.append(65)
        assert lut.head.data == 342
        assert lut.tail.data == 65
        assert lut.head.next == lut.tail
        assert lut.tail.previous == lut.head

        lut.append(94)
        assert lut.head.data == 342
        assert lut.tail.data == 94
        assert lut.head.next.data == 65
        assert lut.head.next.next.data == 94

