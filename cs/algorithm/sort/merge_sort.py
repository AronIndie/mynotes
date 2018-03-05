# -*- coding:utf-8 -*-
"""
归并排序

通过合并两个已排序的序列，进行输出

合并序列需要最多经过 N-1次比较，分治法复杂度为O(logN)，所以最坏情况为O(NlogN)

最好 O(N)
最坏 O(NlogN)
平均 O(NlogN)

"""

def merge(a: list, b: list) -> list:
    a_ctr = 0
    b_ctr = 0
    res = []
    while a_ctr < len(a) and b_ctr < len(b):
        if a[a_ctr] <= b[b_ctr]:
            res.append(a[a_ctr])
            a_ctr += 1
        else:
            res.append(b[b_ctr])
            b_ctr += 1

    if a_ctr == len(a):
        res += b[b_ctr:]
    elif b_ctr == len(b):
        res += a[a_ctr:]

    return res

def merge_sort(a: list) -> list:

    if len(a) == 1:
        return a

    split_point = len(a) // 2
    left = merge_sort(a[:split_point])
    right = merge_sort(a[split_point:])

    return merge(left, right)
