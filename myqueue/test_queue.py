import pytest

from .queue import Queue, ArrayQueue

# @pytest.mark.parametrize("queue_class", [Queue, ArrayQueue])
# @pytest.mark.parametrize("queue_class", [Queue])
# def test_basic(queue_class):
#     qut = queue_class()
#     assert qut.is_empty() is True

#     with pytest.raises(Exception):
#         qut.remove()

#     with pytest.raises(Exception):
#         qut.peek()

#     qut.add(4)
#     assert qut.is_empty() is False

#     qut.add(5)
#     assert qut.peek() == 4
#     assert qut.remove() == 4
#     assert qut.remove() == 5
#     assert qut.is_empty() is True

class TestArrayQueue:
    def test_basic(self):
        qut = ArrayQueue()
        qut.add(5)
        qut.add(3)

        assert qut.peek() == 5
        assert qut.remove() == 5
        assert qut.is_empty() is False
        assert len(qut.storage) == 2

        qut.add(4)
        qut.add(6)
        assert len(qut.storage) == 3
        assert qut.remove() == 3
        assert qut.remove() == 4
        assert qut.remove() == 6


        assert qut.is_empty() is True

