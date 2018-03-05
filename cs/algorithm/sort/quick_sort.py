# -*- coding:utf-8 -*-

"""
快速排序（同样适用了分治、递归）

每次迭代均使得基准左侧的值小于基准，基准右侧的值大于基准
"""

def median_3(a: list, left: int, right: int):
    """
    三数中值取基准
    """
    center = (left + right) // 2
    median_value = a[center]
    left_value = a[left]
    right_value = b[right]
    if median_value < left_value:
        left_value, median_value = median_value, left_value
    if median_value > right_value:
        right_value, median_value = median_value, right_value
    if right_value < left_value:
        right_value, left_value = left_value, right_value

    return median_value

def quick_sort(a: list) -> list:

    if len(a) in [0, 1]:
        return a

    if len(a) == 2:
        if a[0] <= a[1]:
            return a
        else:
            return [a[1], a[0]]

    pivot = a[-1] #median_3(a, 0, len(a)-1)

    left = 0
    right = len(a) - 2

    while left < right:

        while a[left] < pivot and left < right:
            left += 1

        while a[right] > pivot and left < right:
            right -= 1

        a[left], a[right] = a[right], a[left]

    a[left], a[-1] = a[-1], a[left]

    print(a, pivot)
    left_array = quick_sort(a[:left])
    right_array = quick_sort(a[left+1:])

    return left_array + [pivot] + right_array
