# -*- coding:utf-8 -*-

from utils.tree import *

class Solution:
    def isSymmetric(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return True

        return self.judge(root.left, root.right)

    def judge(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False

        if root1.value == root2.value:
            return self.judge(root1.left, root2.right) and self.judge(root1.right, root2.left)

        return False


if __name__ == '__main__':
    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node1.left = node2
    node1.right = node2
    #node3.left = node4

    a = Solution()
    print(a.isSymmetric(node1))


