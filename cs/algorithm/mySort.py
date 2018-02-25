# -*- coding:utf-8 -*-
import os
import time
import numpy as np
import random

def bucksetSort(arr : list):
    maxNum = max(arr)
    minNum = min(arr)
    bucketNums = (maxNum - minNum) // 10 # 先按照0-9, 10-19分桶
    bucketNums += 1
    buckets = []
    for i in range(bucketNums):
        buckets.append([])
    for i in arr:
        whichBuckets = i//10
        buckets[whichBuckets].append(i)

    ## 此时对buckets每个内容进行插入排序
    for i,bucket in enumerate(buckets):
        if bucket == []:
            pass
        if len(bucket) == 1:
            pass

        new_bucket = insertionSort(bucket)
        buckets[i] = new_bucket
    return buckets

def bucksetSort2(arr : list) -> list:
    """
    递归调用桶排序
    """
    if len(arr) == 1:
        return arr

    bucksetSize = 10 if len(arr) > 10 else 1
    bucksetNum = (max(arr) - min(arr)) // bucksetSize + 1
    bucksets = [[] for i in range(bucksetNum)]
    for i in arr:
        bucksets[(i - min(arr)) // bucksetSize].append(i)

    for i, buckset in enumerate(bucksets):
        if buckset == []:
            pass
        elif len(buckset) == 1:
            bucksets[i] = buckset
        else:
            bucksets[i] = bucksetSort2(buckset)

    return sum(bucksets, [])

def insertionSort(arr :list):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j-=1
        arr[j] = temp
    return arr

a = [1,3,4,2,5,0,9,8,6,7,10,12,13]
b = random.sample(range(1000), 1000)
# new_a = insertionSort(a)
new_a = bucksetSort2(b)
print(new_a)





















