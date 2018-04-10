# -*- coding:utf-8 -*-


def foo(num, b):
    res = []
    while num > 0:
        res.append(num % b)
        num //= b
    res.reverse()
    return res

if __name__ == '__main__':
    n = 21
    count = 0
    for i in range(1, n + 1):
        s1 = foo(i, 2)
        s2 = [int(i) for i in list(str(n))]
        if sum(s1) == sum(s2):
            print(i, s1, s2)
            count += 1
