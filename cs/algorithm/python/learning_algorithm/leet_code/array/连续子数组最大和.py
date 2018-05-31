# -*- coding:utf-8 -*-

def foo(arr):
    cur, _max = 0, 0
    for i in arr:
        cur = max(0, cur+i)
        _max = max(cur, _max)
    return _max

if __name__ == '__main__':
    print(foo([6, -3, -2, 7, -15, 1, 2, 2]))
