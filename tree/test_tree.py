from .tree import BinarySearchTree, BinaryNode, BinaryTree


class TestBinarySearchTree:
    def test_single_element_insert(self):
        assert list(BinarySearchTree([3])) == [3]

    def test_two_element_insert(self):
        assert list(BinarySearchTree([1,3])) == [3,1]

    def test_insert_multiple_elements(self):
        tut = BinarySearchTree(
            [1,2,3,5,6,7,8]
        )

        #        5
        #    2       7
        #  1   3   6   8

        assert list(tut) == [5,2,7,1,3,6,8]

class TestBinaryTree:
    def test_equal(self):
        bt = BinaryTree()
        bt.root = BinaryNode(
            1,
            BinaryNode(2, BinaryNode(4, BinaryNode(5))),
            BinaryNode(3, None, BinaryNode(6, None, BinaryNode(7)))
        )

        other = BinaryTree()
        other.root = BinaryNode(
            1,
            BinaryNode(2, BinaryNode(4, BinaryNode(5))),
            BinaryNode(3, None, BinaryNode(6, None, BinaryNode(7)))
        )

        assert bt == other

        assert BinaryTree() == BinaryTree()

    def test_equal(self):
        bt = BinaryTree()
        bt.root = BinaryNode(
            1,
            BinaryNode(2, BinaryNode(4, BinaryNode(5))),
            BinaryNode(3, None, BinaryNode(6, None, BinaryNode(7)))
        )

        other = BinaryTree()
        other.root = BinaryNode(
            1,
            BinaryNode(2, BinaryNode(4, BinaryNode(5))),
            BinaryNode(3, None, BinaryNode(6, None, BinaryNode(8))) # last node here is different 7 !=  7
        )

        assert bt != other

    def test_insert(self):
        #         1
        #       2   3
        #     4       5
        #   6           7
        bt = BinaryTree([1,2,3,4,None,None,5,6,None,None,7])
        other = BinaryTree()
        other.root = BinaryNode(
            1,
            BinaryNode(2, BinaryNode(4, BinaryNode(6))),
            BinaryNode(3, None, BinaryNode(5, None, BinaryNode(7)))
        )

        assert bt == other

    def test_is_balanced(self):
        bt = BinaryTree()

        # [3,9,20,null,null,15,7]

        bt.root = BinaryNode(
            3,
            BinaryNode(9),
            BinaryNode(20, BinaryNode(15), BinaryNode(7))
        )

        assert bt.is_balanced() == True

    def test_is_NOT_balanced(self):
        bt = BinaryTree()

        # [1,2,2,3,None,None,3,4,None,None,4]

        bt.root = BinaryNode(
            1,
            BinaryNode(2, BinaryNode(3, BinaryNode(4))),
            BinaryNode(2, None, BinaryNode(3, None, BinaryNode(4)))
        )

        assert bt.is_balanced() == False

    def test_lists_for_depth(self):
        assert BinaryTree().lists_for_depth() == []

        #       1
        #     2   3
        #   4       5
        # 6           7

        bt = BinaryTree([1,2,3,4,None,None,5,6,None,None,7])
        assert bt.lists_for_depth() == [
            [1], [2,3], [4,5], [6,7]
        ]
