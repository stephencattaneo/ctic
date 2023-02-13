class Node:
    value = None
    children = None

    def __init__(self, value) -> None:
        self.value = value
        self.children = []

class BinaryNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    root = None

    def __init__(self, items = None) -> None:
        if items:
            try:
                self.__build(items)
            except IndexError:
                pass # inserts complete

    def __build(self, items) -> None:
        self.root = BinaryNode(items.pop(0))
        cursors = [self.root]

        while True:
            cursor = cursors.pop(0)
            item = items.pop(0)
            if item is not None:
                cursor.left = BinaryNode(item)
                cursors.append(cursor.left)

            item = items.pop(0)
            if item is not None:
                cursor.right = BinaryNode(item)
                cursors.append(cursor.right)

    def __iter__(self):
        self.iter_queue = []
        if self.root is not None:
            self.iter_queue.append(self.root)
        return self

    def __next__(self) -> list:
        try:
            cursor = self.iter_queue.pop(0)
        except IndexError:
            raise StopIteration

        if cursor.left is not None:
            self.iter_queue.append(cursor.left)

        if cursor.right is not None:
            self.iter_queue.append(cursor.right)

        return cursor.value


    def __str__(self) -> str:
        return str(list(self))

    def is_balanced(self) -> bool:
        '''
          Use an auxillary function. Return an out of bounds value if a node has height more than at any level. (Alternatively raise an exception.)
        '''
        return self.__balancedAux(self.root) >= 0

    def __balancedAux(self, root):
        if root is None:
            return 0

        leftchild = self.__balancedAux(root.left)
        rightchild = self.__balancedAux(root.right)
        if abs(leftchild - rightchild) > 1 or leftchild < 0 or rightchild < 0:
            return -1

        return 1 + max(leftchild, rightchild)

    def __eq__(self, other: object) -> bool:
        return self.__equiv_tree(self.root, other.root)

    def __equiv_tree(self, self_node, other_node):
        if self_node is None:
            return other_node is None

        return self_node.value == other_node.value and \
            self.__equiv_tree(self_node.left, other_node.left) and \
            self.__equiv_tree(self_node.right, other_node.right)

    def lists_for_depth(self) -> list:
        cursor = (self.root, 0)
        queue = []
        return_value = []

        while cursor:
            if cursor[0] is not None:
                try:
                    depth_list = return_value[cursor[1]]
                except IndexError:
                    depth_list = []

                depth_list.append(cursor[0].value)

                try:
                    return_value[cursor[1]] = depth_list
                except IndexError:
                    return_value.append(depth_list)

                queue.append((cursor[0].left, cursor[1] + 1))
                queue.append((cursor[0].right, cursor[1] + 1))

            try:
                cursor = queue.pop(0)
            except IndexError:
                cursor = None

        return return_value


class BinarySearchTree(BinaryTree):
    root = None

    def __init__(self, items = None) -> None:
        if items:
            # assume sorted list
            self.root = self.__build(items, 0, len(items) - 1)

    def __build(self, items, start, end):
        '''
        Leverage that the list is sorted.
        Find the middle, use recusion populate right and left.
        '''
        if end < start:
            return

        middle = ((end - start + 1) // 2) + start
        root = BinaryNode(items[middle])
        root.left = self.__build(items, start, middle - 1)
        root.right = self.__build(items, middle + 1, end)

        return root
