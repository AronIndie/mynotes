# -*- coding:utf-8 -*-
"""
冒泡排序
ref：https://www.cnblogs.com/chengxiao/p/6103002.html
"""

def bubble_sort(a: list) -> list:
    length = len(a)
    for i in range(length):
        for j in range(1, length - i):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]

    return a

