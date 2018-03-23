# -*- coding:utf-8 -*-


def top(a, k):
    heap = a[:k]

    for i in range(k // 2- 1, -1, -1):
        adj_heap(heap, i, k)

    for i in a[k:]:
        if i > heap[0]:
            heap[0] = i
            adj_heap(heap, 0, k)
    return heap


def adj_heap(a, i, length):

    temp = a[i]
    k = 2 * i + 1
    while k < length:
        if k + 1 < length and a[k] > a[k + 1]:
            k += 1

        if temp > a[k]:
            a[i] = a[k]
            i = k
        else:
            break
        k = 2 * k + 1
    a[i] = temp



"""
最快的方法：快排思路
如果是找第k小的数也是类似
"""
def find_top_k(arr, i, j, k):
    if not arr or k == 0 or k > len(arr):
        return []

    l, r = i, j
    flag = arr[j]
    while i < j:
        while i < j and arr[i] <= flag:
            i += 1
        arr[j] = arr[i]
        while i < j and arr[j] > flag:
            j -= 1
        arr[i] = arr[j]
    arr[i] = flag
    if k == i:
        return arr[:i]
    elif i > k:
        return find_top_k(arr, l, i-1, k)
    else:
        return find_top_k(arr, i+1, r, k)



if __name__ == '__main__':
    import numpy as np
    np.random.seed(10)
    a = np.random.choice(np.arange(100), 100, replace=False)
    print(top(a, 10))

    a = [3,2,5,1,4,6,9,1,2,7]
    print(find_top_k(a, 0, len(a) - 1, 5))
