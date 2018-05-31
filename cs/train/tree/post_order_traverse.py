# -*- coding:utf-8 -*-

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pot(root):
    stack = [root]
    flag = {root: False}
    while stack:
        temp = stack[-1]

        if not flag[temp]:
            if temp.right:
                stack.append(temp.right)
                flag[temp.right] = False
            if temp.left:
                stack.append(temp.left)
                flag[temp.left] = False
            flag[temp] = True

        else:
            print(stack.pop().value)

if __name__ == '__main__':
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node10 = Node(10)
    node6.left = node10
    pot(root)