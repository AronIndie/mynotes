# -*- coding:utf-8 -*-


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(node):
    if not node or not node.next:
        return node

    p = node
    q = node.next
    r = q.next
    q.next = p
    p.next = None
    while r:
        p = q
        q = r
        r = r.next
        q.next = p

    return q


def print_node(node):
    while node:
        print(node.value)
        node = node.next


if __name__ == '__main__':
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node.next = node3
    node3.next = node2
    node2.next = node4
    r = reverse_linked_list(node)
    print_node(r)



