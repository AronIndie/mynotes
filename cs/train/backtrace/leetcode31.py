# -*- coding:utf-8 -*-


"""
https://leetcode.com/problems/next-permutation/#/description

字典序问题

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                temp = i
                break
        if temp == 0:
            nums.sort()
            return

        for i in range(len(nums)-1, temp-1, -1):
            if nums[i] > nums[temp-1]:
                nums[temp-1], nums[i] = nums[i], nums[temp-1]
                break
        nums[temp:] = sorted(nums[temp:])


if __name__ == '__main__':
    s = Solution()
    nums = [1,3,2,4]
    s.nextPermutation(nums)
    print(nums)
