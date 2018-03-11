# -*- coding:utf-8 -*-

from utils.tree import *

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = [(1, root)]
        count = 0
        node_of_this_level = []
        res = []
        while len(queue) != 0:
            temp = queue.pop()
            if count < temp[0]:
                if node_of_this_level != []:
                    res.insert(0, node_of_this_level)
                node_of_this_level = []
                count = temp[0]
            node_of_this_level.append(temp[1].value)

            if temp[1].left is not None:
                queue.insert(0, (count + 1, temp[1].left))
            if temp[1].right is not None:
                queue.insert(0, (count + 1, temp[1].right))

        if node_of_this_level != []:
            res.insert(0, node_of_this_level)
        return res

if __name__ == '__main__':
    node1 = TreeNode(0)
    node2 = TreeNode(1)
    node3 = TreeNode(2)
    node4 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node3.left = node4

    a = Solution()
    print(a.levelOrderBottom(node1))


