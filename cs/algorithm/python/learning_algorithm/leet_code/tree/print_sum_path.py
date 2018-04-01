# -*- coding:utf-8 -*-

"""
剑指offfer 二叉树中和为某一值的路径
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        temp = []
        self.get_path(root, expectNumber, temp)
        return self.res

    res = []
    def get_path(self, root, value, temp):
        if not root or value < root.val:
            return

        if value == root.val and not root.left and not root.right:
            temp.append(root.val)
            self.res.append(temp[:])
        else:
            temp.append(root.val)
            self.get_path(root.left, value - root.val, temp)
            self.get_path(root.right, value - root.val, temp)

if __name__ == '__main__':
    root = TreeNode(10)
    node1 = TreeNode(5)
    node2 = TreeNode(12)
    node3 = TreeNode(4)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    s = Solution()
    print(s.FindPath(root, 15))