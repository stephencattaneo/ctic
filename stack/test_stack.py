from pytest import raises

from .stack import Stack

def test_sanity():
    sut = Stack()
    assert sut.is_empty() is True

    sut.push(3)
    assert sut.is_empty() is False

    assert sut.peek() == 3
    assert sut.pop() == 3

    assert sut.is_empty() is True

    with raises(Exception):
        sut.pop()

    with raises(Exception):
        sut.peek()




