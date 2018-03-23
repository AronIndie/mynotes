# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        pass



def gen_list_node(lst):
    n = ListNode(lst[0])
    p = n
    for i in range(1, len(lst)):
        temp = ListNode(lst[i])
        n.next = temp
        n = temp
    return p


if __name__ == '__main__':
    l = gen_list_node([1,2,3,3,4,4,5])
    s = Solution()
    s.deleteDuplication(l)