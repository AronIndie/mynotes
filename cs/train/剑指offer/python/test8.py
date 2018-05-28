# -*- coding:utf-8 -*-


"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0: return 0
        if number == 1: return 1
        if number == 2: return 2

        p = 1
        q = 2

        for i in range(3, number+1):
            r = p + q
            p = q
            q = r
        return r

