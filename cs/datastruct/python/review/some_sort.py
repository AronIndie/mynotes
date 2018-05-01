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


def


if __name__ == '__main__':
    test_case = [3,4,2,1,5]
    # print(insert_sort(test_case))
    # print(insert_sort(bubble_sort(test_case)))
    # print(choose_sort(test_case))
    print(shell_sort(test_case))