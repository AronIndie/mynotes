# -*- coding:utf-8 -*-

"""
科室素拓进行游戏，游戏规则如下：随机抽取9个人作为游戏参与人员，分别编号1至9，每轮要求k(k<=9且k>=0)个人自由组合使编号之和为n。
输出满足规则的所有可能的组合。要求组合内部编号升序输出，组合之间无顺序要求。
"""

#  inp = raw_input()
#k, n = inp.split(" ")
k = 3 #int(k)
n = 15 #int(n)
res = []


def foo(k, n, s, c):
    if k == 1:
        if s <= n <= 9:
            c.append(n)
            temp = c.copy()
            if temp not in res:
                res.append(temp)
            c.pop()
    if s > 9:
        return
    foo(k, n, s + 1, c.copy())
    c.append(s)
    foo(k - 1, n - s, s + 1, c.copy())
    c.pop()


foo(k, n, 1, [])
print(res)


