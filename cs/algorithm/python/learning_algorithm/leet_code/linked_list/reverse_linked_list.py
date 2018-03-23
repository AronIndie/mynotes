# -*- coding:utf-8 -*-

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(head: Node):
    if head is None or head.next is None:
        return head

    p = head
    q = head.next
    r = q.next

    q.next = p
    p.next = None

    while r is not None:
        p = q
        q = r
        r = q.next
        q.next = p

    return q


def display(head: Node):
    while head is not None:
        print(head.value)
        head = head.next

if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node1.next.next.next = Node(4)

    display(node1)
    display(reverse_list(node1))