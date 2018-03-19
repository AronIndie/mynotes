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


if __name__ == '__main__':
    import numpy as np
    np.random.seed(10)
    a = np.random.choice(np.arange(100), 100, replace=False)
    print(top(a, 10))
