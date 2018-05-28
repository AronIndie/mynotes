# -*- coding:utf-8 -*-


"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

# -*- coding:utf-8 -*-
class Solution:
    dic = {}
    def jumpFloorII(self, number):
        # write code here
        if number == 0: return 0
        if number == 1: return 1
        
        if number in self.dic:
            return self.dic[number]
        else:
            sum = 0
            for i in range(number):
                if i in self.dic:
                    sum += self.dic[i]
                else:
                    temp = self.jumpFloorII(i)
                    self.dic[i] = temp
                    sum += temp
            self.dic[number] = sum + 1
            return sum + 1
