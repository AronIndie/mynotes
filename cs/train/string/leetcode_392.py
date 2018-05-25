# -*- coding:utf-8 -*-

"""
给定字符串s和t，判断s是否是t的子序列
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        i = 0
        while i < len(s):
            idx = t.find(s[i], start)
            if idx == -1:
                return False
            i += 1
            start = idx + 1
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence('abc', 'adsbiocp'))

