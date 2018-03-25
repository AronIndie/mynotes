# -*- coding:utf-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        q = None
        dic = {}
        c = pHead
        while pHead:
            p = RandomListNode(pHead.label)
            dic[pHead] = p
            if q:
                q.next = p
            else:
                res = p
            q = p
            pHead = pHead.next

        for i in dic:
            if i.random:
                dic[i].random = dic[i.random]
            else:
                dic[i].random = None
        # temp = res
        # while temp:
        #     temp.random = dic[id(c.random)]
        #     temp = temp.next
        #     c = c.next

        return res

if __name__ == '__main__':
    a1 = RandomListNode(1)
    a2 = RandomListNode(2)
    a3 = RandomListNode(3)
    a4 = RandomListNode(4)
    a5 = RandomListNode(4)

    a1.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5

    a1.random = a3
    a2.random = a5
    a4.random = a2

    s = Solution()
    temp = s.Clone(a1)
    print(temp)