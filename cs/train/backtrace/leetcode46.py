# -*- coding:utf-8 -*-


"""
https://leetcode.com/problems/permutations/description/

Given a collection of distinct integers, return all possible permutations.

全排列问题
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtrace(nums, 0)
        return self.res

    def backtrace(self, nums, i):
        if i >= len(nums):
            self.res.append(nums[:])

        else:
            # 有重复数字时，记录是否使用过
            used = []
            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue
                else:
                    used.append(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                self.backtrace(nums, i+1)
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3,3]))