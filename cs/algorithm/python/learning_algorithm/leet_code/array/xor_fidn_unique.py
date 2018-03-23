# -*- coding:utf-8 -*-

from functools import reduce

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return []

        temp = 0
        for i in array:
            temp ^= i

        b = bin(temp)[2:]
        for i in range(len(b)-1, -1, -1):
            if b[i] == '1': break
        i = len(b) - i

        g1 = []
        g2 = []
        for j in array:
            if bin(j)[-i] == '0':
                g1.append(j)
            else:
                g2.append(j)

        return [reduce(lambda x, y: x ^ y, g1), reduce(lambda x, y: x ^ y, g2)]

if __name__ == '__main__':
    a = [2,4,3,6,3,2,5,5]
    s = Solution()
    print(s.FindNumsAppearOnce(a))