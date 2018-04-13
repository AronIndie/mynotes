# -*- coding:utf-8 -*-


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

res = None
def reverse(node):
    global res
    if not node.next:
        res = node
        return node
    tail = reverse(node.next)
    node.next = None
    tail.next = node
    return node

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.next = n3
    n3.next = n2
    n2.next = n4

    reverse(n1)
    print(res)
