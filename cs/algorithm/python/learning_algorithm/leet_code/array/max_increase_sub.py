# -*- coding:utf-8 -*-

"""
求最大递增子序列
"""

def foo(arr):
    res = [1 for i in range(len(arr))]
    # res[0] = 1
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] < arr[i]:
                res[i] = max(res[i], res[j]+1)
    return max(res)

if __name__ == '__main__':
    print(foo([2,1,5,3,6,4,8,9,7]))




