# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        init = num[:size]
        _max = self.find_max(init)
        res = [_max[1]]
        for i in range(size, len(num)):
            if num[i] >= _max[1]:
                res.append(num[i])
            else:
                if _max[0] + size > i:
                    _max = self.find_max(num[i - 2:i + 1])
                    res.append(_max[1])
                else:
                    res.append(_max[1])
        return res

    def find_max(self, arr):
        _max = [0, arr[0]]
        for i, num in enumerate(arr):
            if i != 0:
                if num >= _max[0]:
                    _max = [i, num]
        return _max

if __name__ == '__main__':
    s = Solution()
    print(s.maxInWindows([2,3,4,2,6,2,5,1],3))