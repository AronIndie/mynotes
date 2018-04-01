# -*- coding:utf-8 -*-

"""

串项链问题，给定每个珍珠的数量下限和上限，求串一个长度为m的向量的方案总数
"""


def foo(init, m):
    if m == 0 or len(init) == 0:
        return 1

    if len(init) == 1 :
        if m > init[0][1]:
            return 0
        else:
            return 1

    if sum(list(zip(*init))[0]) > m:
        return 0
    s = 0
    for i in range(init[0][0], init[0][1]+1):
        if i <= m:
            s += foo(init[1:], m - i)
    return s

init = [[0,3], [0,3], [0,3]]
m = 5
print(foo(init, m))