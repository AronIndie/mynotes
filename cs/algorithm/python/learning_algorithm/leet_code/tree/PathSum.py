# -*- coding:utf-8 -*-

from utils.tree import *



class Solution:
    def hasPathSum(self, root, the_sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        self.get_path(root, 0, the_sum)
        return self.flag

    flag = False

    def get_path(self, root, above_value, the_sum):
        if root is None:
            return

        if root.left is None and root.right is None:
            if  above_value + root.value == the_sum:
                self.flag = True
            return

        self.get_path(root.left, above_value + root.value, the_sum)
        self.get_path(root.right, above_value + root.value, the_sum)

if __name__ == '__main__':
    node1 = TreeNode(5)
    node2 = TreeNode(3)
    node3 = TreeNode(2)
    node4 = TreeNode(4)

    node1.left = node2
    node1.right = node3
    #node3.left = node4
    a = Solution()
    print(a.hasPathSum(node1, 5))