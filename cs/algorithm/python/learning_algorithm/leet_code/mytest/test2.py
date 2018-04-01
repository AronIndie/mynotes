# -*- coding:utf-8 -*-

"""
输入包括两行, 第一行包括两个正整数n和s(1 <= n <= 10, 1 <= s <= 1000), 表示妞妞的硬币个数和需要支付的车费。
第二行包括n个正整数p[i] (1 <= p[i] <= 100)，表示第i个硬币的价值。
保证妞妞的n个硬币价值总和是大于等于s。
"""
w = [4,1,3,5,4]

res = []
def foo(s, c):
    if res:
        _min_coin = min([w[-i] for i in res])
        if c <= - _min_coin:
            return -1
    if s < 1:
        return 0
    if s == 1 and c > w[s]:
        return 0


    l = foo(s-1, c)
    res.append(s)
    r = foo(s-1, c-w[-s]) + 1
    res.remove(s)
    return max(l, r)

print(foo(len(w), 9))