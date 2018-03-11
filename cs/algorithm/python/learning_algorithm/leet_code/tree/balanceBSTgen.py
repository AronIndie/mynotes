# -*- coding:utf-8 -*-

from utils.tree import *

"""
根据所给的有序数组建立平衡二叉搜索树
"""
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if nums == []:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])


        center = len(nums) // 2
        node = TreeNode(nums[center])

        if nums[: center] != []:
            node.left = self.sortedArrayToBST(nums[: center])
        else:
            node.left = None

        if nums[center + 1: ] != []:
            node.right = self.sortedArrayToBST(nums[center + 1: ])
        else:
            node.right = None

        return node





if __name__ == '__main__':

    a = Solution()
    res = a.sortedArrayToBST([1,2,3,4,5,6,7,8,9])
    print(res)



