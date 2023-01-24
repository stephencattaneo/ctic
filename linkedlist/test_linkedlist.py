from .list import List, DoubleList

def test_emptylist_append():
    lut = List()
    assert lut.head is None

    lut.append(5)
    assert lut.head.data == 5
    assert lut.head.next is None

def test_singlelist_multiple_items():
    lut = List()

    lut.append(6)
    lut.append(3)

    assert lut.head.data == 6
    assert lut.head.next.data == 3

def test_emptydouble_append():
    lut = DoubleList()
    assert lut.head is None
    assert lut.tail is None

    lut.append(9)
    assert lut.head == lut.tail
    assert lut.head.data == 9

def test_doublelist_multiple_items():
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

