# -*- coding:utf-8 -*-

"""
排序算法测试
"""
from utils.time_it import timeit

@timeit
def insert_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
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


def quick_sort(arr: list, l: int, r: int):
    if l >=r:
        return

    flag = arr[r]
    low = l
    high = r
    while l < r:
        while l < r and arr[l] < flag:
            l += 1
        arr[r] = arr[l]

        while l < r and arr[r] > flag:
            r -= 1
        arr[l] = arr[r]

    arr[l] = flag
    quick_sort2(arr, low, l - 1)
    quick_sort2(arr, l + 1, high)



def quick_sort2(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] < key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort2(array, low, left - 1)
    quick_sort2(array, left + 1, high)


if __name__ == '__main__':
    a = [0, 3,1,2,5,7,8,6,4,20]
    insert_sort(a)
    #print(insert_sort(a))
    #print(bubble_sort(a))
    #print(merge([1,3,5,9], [2,4,10,11]))
    #print(merge_sort(a))

    # import numpy as np
    # np.random.seed(10)
    # a = np.random.choice(np.arange(10000), 1000, replace=False)
    # import time
    #
    # time1 = time.time()
    # #quick_sort(a)
    # #insert_sort(a)
    # #merge_sort(a)
    # time2 = time.time()
    # print(time2 - time1)
    # insert_sort(a)
    #quick_sort(a, 0, len(a)-1)
    print(a)