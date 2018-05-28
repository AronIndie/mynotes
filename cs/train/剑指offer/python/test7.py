# -*- coding:utf-8 -*-


"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0: return 0
        if n == 1: return 1
        p = 0
        q = 1
        r = p + q
        for i in range(2, n+1):
            r = p + q
            p = q
            q = r
        return r
