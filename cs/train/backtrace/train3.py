# -*- coding:utf-8 -*-

"""
Leetcode 39. https://leetcode.com/problems/combination-sum/description/


Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.


attention:
- all positive
- can duplicate
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.candidates = candidates
        self.backtrace([], target)
        return self.res

    def backtrace(self, sub, target):
        if target == 0:
            self.res.append(sub[:])
            return

        for i in self.candidates:
            if target >= i:
                if sub == [] or (sub != [] and sub[-1] <= i):
                    self.backtrace(sub + [i], target - i)


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 5], 8))
