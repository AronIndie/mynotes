# -*- coding:utf-8 -*-

"""
排序算法测试
"""
from utils.time_it import timeit

@timeit
def insert_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        temp = arr[i]

        for j in range(i, 0, -1):
            if temp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                j += 1
                break
        arr[j-1] = temp
    return arr

def bubble_sort(arr: list) -> list:
    for j in range(len(arr)):
        for i in range(1, len(arr) - j):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i-1]
    return arr

def merge(arr1, arr2) -> list:
    if arr1 == []:
        return arr2
    if arr2 == []:
        return arr1

    i = 0
    j = 0
    res = []
    while 1:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j +=1

        if i >= len(arr1):
            res += arr2[j:]
            break
        if j >= len(arr2):
            res += arr1[i:]
            break
    return res


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    center = len(arr) // 2
    left = merge_sort(arr[:center])
    right = merge_sort(arr[center:])

    return merge(left, right)


THRESHOLD = 4

def three_median(arr):
    center = len(arr) // 2
    if arr[0] > arr[center]:
        arr[center], arr[0] = arr[0], arr[center]
    if arr[0] > arr[-1]:
        arr[-1], arr[0] = arr[0], arr[-1]
    if arr[-1] < arr[center]:
        arr[center], arr[-1] = arr[-1], arr[center]

    arr[-1], arr[center] = arr[center], arr[-1]
    return arr


def quick_sort(arr: list) -> list:
    if len(arr) <= 1:
        return  arr

    if len(arr) <= THRESHOLD:
        return insert_sort(arr)

    three_median(arr)
    flag = arr[-1]
    i = 0
    j = len(arr) - 2
    while i < j:

        while arr[i] < flag and i < j:
            i += 1
        while arr[j] > flag and i < j:
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[-1] = arr[-1], arr[i]

    left = quick_sort(arr[: i])
    right = quick_sort(arr[i+1: ])

    return list(left) + [flag] + list(right)



if __name__ == '__main__':
    a = [3,1,2,5,7,8,6,4]
    #print(insert_sort(a))
    #print(bubble_sort(a))
    #print(merge([1,3,5,9], [2,4,10,11]))
    #print(merge_sort(a))

    import numpy as np
    np.random.seed(10)
    a = np.random.choice(np.arange(10000), 1000, replace=False)
    import time

    time1 = time.time()
    #quick_sort(a)
    #insert_sort(a)
    #merge_sort(a)
    time2 = time.time()
    print(time2 - time1)
    insert_sort(a)