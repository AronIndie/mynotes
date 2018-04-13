# -*- coding:utf-8 -*-


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def gen_tree(arr):
    if len(arr) == 0:
        return None
    nodes = [Node(i) if i != "#" else None for i in arr]
    for i in range(len(nodes) // 2 - 1, -1, -1):
        k = 2 * i + 1
        if k < len(nodes):
            nodes[i].left = nodes[k]
        if k + 1 < len(nodes):
            nodes[i].right = nodes[k+1]
    return nodes[0]


def pre_order_traverse(root):
    if not root:
        return
    print(root.value)
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)

def in_order_traverse(root):
    if not root:
        return
    pre_order_traverse(root.left)
    print(root.value)
    pre_order_traverse(root.right)

def post_order_traverse(root):
    if not root:
        return
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)
    print(root.value)

def pre_order_traverse_NC(root):
    stack = [root]
    while stack:
        temp = stack.pop()
        print(temp.value)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)

def in_order_traverse_NC(root):
    stack = []
    

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8]
    root = gen_tree(arr)
    print(root)
    print(pre_order_traverse(root))
    print(pre_order_traverse_NC(root))


