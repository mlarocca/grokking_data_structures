"""Binary Search Tree (BST) implementation."""
from __future__ import annotations
from stacks.stack import Stack

class BinarySearchTree:
    """A class modeling the binary search tree data structure."""

    class Node:
        """A class modeling the nodes of the binary search tree."""

        @staticmethod
        def _node_str(node: type[BinarySearchTree.Node]) -> str:
            return str(node) if node is not None else ''

        def __init__(self, value: any,
                    left: type[BinarySearchTree.Node] = None,
                    right: type[BinarySearchTree.Node] = None) -> None:
            self._value = value
            self._left = left
            self._right = right

        def __str__(self) -> str:
            left_str = BinarySearchTree.Node._node_str(self._left)
            right_str = BinarySearchTree.Node._node_str(self._right)
            return f'{self._value} ({left_str})({right_str})'

        def value(self) -> any:
            """Return the value of the node."""
            return self._value

        def left(self) -> type[BinarySearchTree.Node]:
            """Return a reference to the left child of the node."""
            return self._left

        def right(self) -> type[BinarySearchTree.Node]:
            """Return a reference to the right child of the node."""
            return self._right

        def set_left(self, node: type[BinarySearchTree.Node]) -> None:
            """Set the left child of the node. The old value will be lost."""
            self._left = node

        def set_right(self, node: type[BinarySearchTree.Node]) -> None:
            """Set the right child of the node. The old value will be lost."""
            self._right = node


    def __init__(self) -> None:
        self._root = None


    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'


    def __str__(self) -> str:
        return BinarySearchTree.Node._node_str(self._root)


    def __len__(self) -> bool:
        """Return the number of values stored in the tree."""
        # This version of the traversal algorithm uses an explicit stack, instead of recursion.
        stack = Stack()
        stack.push(self._root)
        size = 0
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                size += 1
                stack.push(node.right())
                stack.push(node.left())
        return size


    def contains(self, value: any) -> bool:
        """Return True if the tree contains the value, False otherwise."""
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return True
            elif value < node_val:
                node = node.left()
            else:
                node = node.right()
        return None


    def insert(self, value: any) -> None:
        """Insert a new value into the tree."""
        parent = None
        node = self._root
        while node is not None:
            parent = node
            if value <= node.value():
                node = node.left()
            else:
                node = node.right()

        if parent is None:
            self._root = BinarySearchTree.Node(value)
        else:
            if value <= parent.value():
                parent.set_left(BinarySearchTree.Node(value))
            else:
                parent.set_right(BinarySearchTree.Node(value))
