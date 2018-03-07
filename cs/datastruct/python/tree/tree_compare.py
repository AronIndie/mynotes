# -*- coding:utf-8 -*-
"""
判断两个二叉树是否相等
"""

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


def compare(node1, node2):

    if (node1 == None and node2 != None) or \
            (node1 != None and node2 == None):
        return False
    elif node1 == node2 == None:
        return True
    else:
        if node1.value == node2.value:
            return compare(node1.left, node2.left) and \
                compare(node1.right, node2.right)

