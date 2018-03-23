# -*- coding:utf-8 -*-
"""
二叉搜索树转双向链表
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        l = self.Convert(pRootOfTree.left)
        r = self.Convert(pRootOfTree.right)
        c = pRootOfTree
        c.left = None
        c.right = None

        if not l:
            return self.concat(c, r)
        elif not r:
            return self.concat(l, c)
        else:
            temp = self.concat(l, c)
            return self.concat(temp, r)

    def concat(self, a, b):
        temp = a
        while temp.right:
            temp = temp.right
        temp.right = b
        b.left = temp

        return a

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node5
    node5.right = node6

    s = Solution()
    a = s.Convert(node4)
    pass