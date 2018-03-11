# -*- coding:utf-8 -*-

from utils.tree import *
from collections import defaultdict
class Solution:
    res = []

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.traverse(root, 0)
        return min(self.res)

    def traverse(self, root, depth):
        if root is None:
            return

        if root.left is None and root.right is None:
            self.res.append(depth + 1)
            return

        self.traverse(root.left, depth + 1)
        self.traverse(root.right, depth + 1)

class Solution2:
    res = []

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return left + right + 1       # 如果是求最大值得话不需要这个
        else:
            return min(left, right) + 1


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node1.left = node2

    a = Solution()
    print(a.minDepth(node1))