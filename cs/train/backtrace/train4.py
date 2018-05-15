# -*- coding:utf-8 -*-


"""
leetcode 77. https://leetcode.com/problems/combinations/description/

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
"""


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.backtrace(n, k, 0, [])
        return self.res

    def backtrace(self, n, k_left, start, sub):
        if k_left == 0:
            self.res.append(sub[:])
            return

        for i in range(start, n):
            if n - i >= k_left:
                self.backtrace(n, k_left - 1, i+1, sub + [i+1])


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))