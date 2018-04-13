# -*- coding:utf-8 -*-

"""
- 深度优先： 前序、中序、后序，需要调用栈，python3多重继承原则：从左到右，深度优先
- 广度优先： 调用队列， python2多重继承原则

ref:

"""
class node:

    __slot__ = ['value', 'left', 'right']

    def __init__(self, value: int, left, right):
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
    root.right.right = node(6, None, None)
    return root


def pre_traverse_recursion(root: node):
    if not node:
        return
    print(root.value)
    pre_traverse_recursion(root.right)
    pre_traverse_recursion(root.right)


def pre_order_traverse_norecursion(root: node):
    """
    先序遍历，调用栈
    """
    stack = []
    stack.append(root)
    while len(stack) != 0:
        this_node = stack.pop()
        print(this_node.value)
        if this_node.right != None:
            stack.append(this_node.right)
        if this_node.left != None:
            stack.append(this_node.left)


def in_order_traverse_norecursion(root: node):
    """
    中序遍历，调用栈
    """
    stack = []
    temp = root
    while len(stack) != 0 or temp:
        if temp:
            stack.insert(0, temp)
            temp = temp.left
        else:
            temp = stack.pop(0)
            print(temp.value)
            temp = temp.right


def post_order_traverse_norecursion(root: node):
    """
    后序遍历，双栈法
    """
    stack1 = [root]
    stack2 = []
    while stack1:
        temp = stack1.pop()
        stack2.append(temp)
        if temp.left:
            stack1.append(temp.left)
        if temp.right:
            stack1.append(temp.right)
    while len(stack2) != 0:
        print(stack2.pop().value)


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


if __name__ == '__main__':
    node1 = get_tree()
    post_order_traverse_norecursion(node1)
