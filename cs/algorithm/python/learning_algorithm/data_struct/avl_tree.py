# -*- coding:utf-8 -*-

from ..utils.tree import TreeNode


"""
待完善。。。
"""

class AVLTree:

    def __init__(self):
        self._root = None
        self.length = None

    def insert(self, value):
        self._root = self._insert(self._root, value)
        self.length += 1

    def _insert(self, root: TreeNode, value) -> TreeNode:
        if not root:
            return TreeNode(value)

        if value < root.value:
            root.left = self._insert(root.left, value)
        elif value > root.value:
            root.right = self._insert(root.right, value)
        else:
            pass

        return root

    def display(self):
        self._display(self._root)

    def _display(self, root, depth=0):
        if not root:
            return

        print(depth*"--"+ " " + str(root.value))
        self._display(root.left, depth+1)
        self._display(root.right, depth+1)

    def left_single_rotate(self, root):
        temp = root
        root = root.left
        temp.left = root.right
        root.right = temp
        return root

    def right_single_rotate(self, root):
        temp = root
        root = root.right
        temp.right = root.left
        root.left = temp
        return root

    def left_double_rotate(self, root):
        root.left = self.right_single_rotate(root.left)
        return self.left_single_rotate(root)

    def right_double_rotate(self, root):
        root.right = self.left_single_rotate(root.right)
        return self.right_single_rotate(root)



