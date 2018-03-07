# -*- coding:utf-8 -*-

from tree.my_node import *
from tree.binary_search_tree import *


class AVLTree(BinarySearchTree):

    def __init__(self):
        super(AVLTree, self).__init__()

    def _height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def _insert(self, node, value):

        if node is None:
            return AVLNode(value, height=0)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            pass
        return self._balance(node)  # 在此处进行AVL树旋转

    def _balance(self, node: AVLNode):
        """
        牢记四种情况，当插入数据时，带来插入节点的父节点的父节点处失衡，记失衡节点为t:
        1. t.left.left 插入
        2. t.right.right 插入
        3. t.left.right 插入
        4. t.right.left 插入
        1,2为同一种情况，使用单旋转；3,4为同一种情况，使用双旋转
        """
        if node is None:
            return None

        if self._height(node.left) - self._height(node.right) > 1:
            if self._height(node.left.left) >= self._height(node.left.right):
                node = self._left_single_rotate(node)
            else:
                node = self._left_double_rotate(node)
        elif self._height(node.left) - self._height(node.right) < -1:
            if self._height(node.right.left) <= self._height(node.right.right):
                node = self._right_single_rotate(node)
            else:
                node = self._right_double_rotate(node)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return node

    def _left_single_rotate(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node

        temp.height = max(self._height(temp.left), self._height(temp.right))+1
        node.height = max(self._height(node.left), self._height(node.right))+1

        return temp

    def _left_double_rotate(self, node):
        node.left = self._right_single_rotate(node.left)
        return self._left_single_rotate(node)

    def _right_single_rotate(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node

        temp.height = max(self._height(temp.left), self._height(temp.right))+1
        node.height = max(self._height(node.left), self._height(node.right))+1

        return temp

    def _right_double_rotate(self, node):
        node.right = self._left_single_rotate(node.right)
        return self._right_single_rotate(node)


if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    avl.insert(4)
    avl.insert(5)
    avl.insert(6)
    avl.insert(7)
    avl.display()
