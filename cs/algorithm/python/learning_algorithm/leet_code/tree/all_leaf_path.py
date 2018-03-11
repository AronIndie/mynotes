# -*- coding:utf-8 -*-

from utils.tree import *

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.judge(root, "")
        return [i[2:] for i in self.res]

    res = []

    def judge(self, root: TreeNode, string: str):
        if not root:
            return
        if not root.left and not root.right:
            string += "->" + str(root.value)
            self.res.append(string)
            return
        
        self.judge(root.left, string + "->" + str(root.value))
        self.judge(root.right, string + "->" + str(root.value))






if __name__ == '__main__':
    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node3.left = node4

    a = Solution()
    print(a.binaryTreePaths(node1))


