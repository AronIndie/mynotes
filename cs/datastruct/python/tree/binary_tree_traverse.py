# -*- coding:utf-8 -*-

"""
- 深度优先： 前序、中序、后序，需要调用栈，python3多重继承原则：从左到右，深度优先
- 广度优先： 调用队列， python2多重继承原则
"""
class node:

    __slot__ = ['value', 'left', 'right']

    def __init__(self, value: str, left: node, right: node):
        self.value = value
        self.left = left
        self.right = right


def get_tree() -> node:

    root = node(0, None, None)
    root.left = node(1, None, None)
    root.right = node(2, None, None)
    root.left.left = node(3, None, None)
    root.left.right = node(4, None, None)
    root.right.left = node(5, None, None)
    return root


def pre_traverse_recursion(root: node):

    print(root.value)
    pre_traverse_norecursion(root.right)
    pre_traverse_norecursion(root.right)


def pre_traverse_norecursion(root: node):
    """
    调用栈
    """
    stack = []
    stack.append(root)

    while len(stack) != 0:
        this_node = stack.pop(0)

        print(this_node.value)
        if this_node.left != None:
            stack.insert(0, this_node.left)
        if this_node.left != None:
            stack.insert(0, this_node.right)


def breadth_first_traverse(root: node):
    """
    调用队列
    """

    queue = []
    queue.append(root)

    while len(queue) != 0:

        this_node = queue.pop(-1)
        print(this_node.value)
        if this_node.left != None:
            queue.insert(0, this_node.left)
        if this_node.right != None:
            queue.insert(0, this_node.left)


