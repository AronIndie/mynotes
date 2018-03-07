# -*- coding:utf-8 -*-

from tree.my_node import *


class BinarySearchTree(object):

    def __init__(self):
        self._clear()

    def _clear(self):
        self._root = None

    def clear(self):
        self._clear()

    def is_empty(self):
        return self._root is None

    def contain(self, value):
        return self._contain(self._root, value)

    def insert(self, value):
        self._root = self._insert(self._root, value)

    def find_min(self):
        return self._find_min(self._root)

    def find_max(self):
        return self._find_max(self._root)

    def remove(self, value):
        return self._remove(self._root, value)

    def display(self):
        self._display(self._root, 1)

    @staticmethod
    def _contain(node, value):
        if node is None:
            return False

        if node.value == value:
            return True
        elif node.value > value:
            return BinarySearchTree._contain(node.left, value)
        else:
            return BinarySearchTree._contain(node.right, value)

    @staticmethod
    def _find_min(node):
        left_value = None
        while node.left is not None:
            left_value = node.left.value
            node = node.left
        return left_value

    @staticmethod
    def _find_max(node):
        right_value = None
        while node.right is not None:
            right_value = node.right.value
            node = node.right
        return right_value

    def _insert(self, node, value):
        """
        不考虑平衡二叉树时候的插入
        """
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            pass

        return node

    @staticmethod
    def _remove(node, value):

        if node is None:
            return None

        if node.value == value:
            if node.left is not None and node.right is not None:
                node.value = BinarySearchTree._find_min(node.right)
                node.right = BinarySearchTree._remove(node.right, node.value)   # 此处上次出错，是node.value 不是 value
            else:
                node = node.left if node.left is not None else node.right
        elif node.value < value:
            node.right = BinarySearchTree._remove(node.right, value)
        else:
            node.left = BinarySearchTree._remove(node.left, value)
        return node

    def _display(self, node, depth):
        if node is None:
            return
        self._display(node.left, depth+1)
        print('-' * 2 * depth + '>' + str(node.value))
        self._display(node.right, depth+1)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(4)
    bst.display()
    print(bst.contain(3))
    print(bst.contain(5))
    print(bst.find_max())
    print(bst.find_min())
    bst.remove(3)
    bst.display()
    print('++++++++++++++')
    bst.insert(3)
    bst.display()
    print('++++++++++++++')
    bst.remove(2)
    bst.display()
