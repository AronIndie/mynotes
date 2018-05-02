# -*- coding:utf-8 -*-

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_order_traverse(node: Node):
    stack = [node]
    while stack:
        top = stack.pop()
        print(top.value)
        if top.right:
            stack.append(top.right)
        if top.left:
            stack.append(top.left)


def in_order_traverse(node: Node):
    stack = []
    temp = node
    while stack or temp:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(temp.value)
            temp = temp.right


def post_order_traverse(node: Node):
    stack = [node]
    dic = {node:True}
    while stack:
        temp = stack[-1]
        if (not temp.right and not temp.left) or dic[temp] == False:
            print(temp.value)
            stack.pop()
            continue
        if temp.right:
            dic[temp] = False
            dic[temp.right] = True
            stack.append(temp.right)
        if temp.left:
            dic[temp] = False
            dic[temp.left] = True
            stack.append(temp.left)

def breadth_first_traverse(node):
    queue = [node]
    while queue:
        temp = queue.pop(0)
        print(temp.value)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node5.left = node7
    breadth_first_traverse(node1)
