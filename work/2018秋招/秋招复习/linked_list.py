# -*- coding:utf-8 -*-


class Node:

    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next


def display(head):
    if head is None:
        print("None")
    else:
        print(head.value)
        while head._next:
            print(head._next.value)
            head = head._next


def get_head():
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    head._next = node2
    node2._next = node3
    node3._next = node4
    return head


def reverse_linked_list(head):
    if head is None or head._next is None:
        return head
    p = head
    q = head._next
    r = q._next
    p._next = None
    q._next = p
    while r:
        p = q
        q = r
        r = r._next
        q._next = p
    return q


def get_k_from_end(head, k):
    p = head
    q = head
    count = 1
    while count < k:
        p = p._next
        if p is None:
            return None
        count += 1
    while p._next:
        p = p._next
        q = q._next
    return q.value




if __name__ == '__main__':
    head = get_head()
    # display(head)
    # rev_head = reverse_linked_list(head)
    # display(rev_head)
    print(get_k_from_end(head, 6))
