# -*- coding:utf-8 -*-

"""
给定一个链表，两个位置，调换这两个位置的元素
"""

from utils.linked_list import *

def reverseBetween(head: Node, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    p = head
    q = p.next
    r = q.next

    for _ in range(m-2):
        p = p.next
        q = p.next
        r = q.next

    r2 = r
    r3 = r

    for _ in range(n-m-2):
        r = r.next
        r3 = r.next

    p.next = r3
    q.next = r3.next
    r3.next = r2
    r.next = q

    return head


def reverseBetween2(head, m, n):

    if m == n: return head
    if m == 1:
        node1 = Node(0)
        node2 = Node(1)
        node1.next= node2
        node2.next = head
        res = reverseBetween2(node1, m+2, n+2)
        return res.next.next

    # 相邻节点
    if n - m == 1:
        p = head
        count = 1
        while count < m-1:
            p = p.next
            count += 1
        q = p.next
        r = p.next.next

        p.next = r
        q.next = r.next
        r.next = q
        return head

    else:
        return reverseBetween(head, m, n)



if __name__ == '__main__':
    head = gen_linked_list(3)
    res = reverseBetween2(head, 1, 3)
    display(res)