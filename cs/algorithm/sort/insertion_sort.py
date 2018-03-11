# -*- coding:utf-8 -*-

def insertion_sort(a: list) -> list:
    """
    算法时间复杂度为:
    - 最差O(N^2)
    - 最好O(N)
    - 平均O(N^2)
    """
    for i, value in enumerate(a):
        if i != 0:
            temp = value
            j = i
            while temp < a[j - 1] and j > 0:
                a[j] = a[j-1]
                j -= 1
            a[j] = temp

    return a


