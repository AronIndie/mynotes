# -*- coding:utf-8 -*-


"""
寻找N个数中前k个最大值
- 可读入内存   O(nlogk)
- 不可读入内存 O(n)
"""

def get_topk1(arr, k):
    # 借助快排实现
    l = 0
    r = len(arr) - 1
    c = get_split_point(arr, l, r)

    while c != k:
        print(c)
        if c > k:
            r = c
            c = get_split_point(arr, l, r-1)
        else:
            l = c
            c = get_split_point(arr, l+1, r)
    return arr[:c]


def get_split_point(arr, l, r):
    flag = arr[r]
    while l < r:
        while l < r and arr[l] < flag:
            l += 1
        arr[r] = arr[l]
        while l < r and arr[r] > flag:
            r -= 1
        arr[l] = arr[r]
    arr[l] = flag
    return l


def get_topk2(arr, k):

    heap = arr[:k]

    for i in range(len(heap) // 2 - 1, -1, -1):
        adj_heap(heap, i)

    for i in arr:
        if i < heap[0]:
            heap[0] = i
            adj_heap(heap, 9)

    return heap

def adj_heap(heap, i):
    # 构造大顶堆，找前k个最小的元素
    temp = heap[i]
    k = 2 * i + 1
    length = len(heap)
    while k < length:
        if k + 1 < length and heap[k + 1] > heap[k]:
            k += 1

        if heap[k] > temp:
            heap[i] = heap[k]
            i = k
        else:
            break
        k = 2 * k +1
    heap[i] = temp


#if __name__ == '__main__':
import numpy as np
a = np.random.choice(np.arange(1000), 1000, replace=False)
print(get_topk1(a, 10))
print(get_topk2(a, 10))
