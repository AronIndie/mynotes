# -*- coding:utf-8 -*-

import numpy as np

def insert_sort(arr):
    for i in range(1, len(arr)):
        temp  = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
        # for j in range(i, 0, -1):
        #     if arr[j-1] > temp:
        #         arr[j] = arr[j-1]
        #     else:
        #         break
        # else:
        #     j -= 1
        # arr[j] = temp
    return arr


def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(1, i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


def choose_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        _max = (-1, -100)
        for j in range(i+1):
            if arr[j] > _max[1]:
                _max = (j, arr[j])
        arr[i], arr[_max[0]] = arr[_max[0]], arr[i]
    return arr


def shell_sort(arr):
    gap = len(arr) // 2
    while gap >= 1:

        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j > 0 and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


def quick_sort(arr, i, j):
    if i >= j:
        return
    target = arr[j]
    l = i
    r = j
    while i < j:
        while i < j and arr[i] <= target:
            i += 1
        arr[j] = arr[i]
        while i < j and arr[j] > target:
            j -= 1
        arr[i] = arr[j]
    arr[i] = target
    quick_sort(arr, l, i-1)
    quick_sort(arr, i+1, r)


def heap_sort(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        adj_heap(arr, i)

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr[: i] = adj_heap(arr[: i], 0)
    return arr


def adj_heap(arr, i):
    """
    小顶堆实现倒序排序
    """
    temp = arr[i]
    k =  2 * i + 1
    while k < len(arr):
        if k + 1 < len(arr) and arr[k+1] < arr[k]:
            k += 1
        if arr[k] < temp:
            arr[i] = arr[k]
            i = k
        else:
            break
        k = 2 * k + 1
    arr[i] = temp
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    center = len(arr) // 2
    left = merge_sort(arr[: center])
    right = merge_sort(arr[center: ])
    return merge(left, right)


def merge(arr1, arr2):
    i, j = 0, 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    if i < len(arr1):
        res += arr1[i:]
    elif j < len(arr2):
        res += arr2[j:]
    return res


def bucket_sort(arr):

    pass


if __name__ == '__main__':
    test_case = [3,4,2,1,5]
    test_case2 = np.arange(100)
    np.random.shuffle(test_case2)
    # print(insert_sort(test_case))
    # print(insert_sort(bubble_sort(test_case)))
    # print(choose_sort(test_case))
    # print(shell_sort(test_case))
    # quick_sort(test_case2, 0, len(test_case2) - 1)
    # print(test_case2)
    # print(heap_sort(test_case2))
    # print(merge_sort(list(test_case2)))
