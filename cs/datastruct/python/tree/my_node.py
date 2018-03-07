# -*- coding:utf-8 -*-

class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class AVLNode(Node):
    def __init__(self, value, left=None, right=None, height=None):
        super(AVLNode, self).__init__(value, left, right)
        self.height = height
