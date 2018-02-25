# -*- coding:utf-8 -*-
import os
import time
import random

"""
快速排序：
    1. 分治法思想，取枢纽元，使得枢纽元左边值全部小于该枢纽元，枢纽元右边的值全部大于该枢纽元，然后再对左右两侧分别排序，如此递归
    2. 枢纽元的选取非常关键
    3. 递归解决，不适用于小数组，适用于较大数组
"""

def QuickSort(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1

            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i], myList[j]= myList[j], myList[i]

            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j], myList[i] = myList[i], myList[j]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base

        #递归前后半区
        QuickSort(myList, start, i - 1)
        QuickSort(myList, j + 1, end)

def QuickSort2(myList, start, end):
    """
    优化1： 减少一般的交换次数
    """
    if start < end:
        i = start
        j = end
        base = myList[start]
        while i<j:
            while (i<j) and (myList[j]) >= base:
                j-=1
            myList[i] = myList[j]
            while (i<j) and (myList[i]) <= base:
                i+=1
            myList[j] = myList[i]

        myList[i] = base
        QuickSort2(myList, start, i-1)
        QuickSort2(myList, i+1, end)

def median3(a, s, e):
    """
    三数中值分割法，寻找第一个数，中间的数，最后一个数中，位于中间的数，并且将其放在数组中间。
    由于此时是引用传递，在内部修改a将会导致外部a同样被修改。
    """
    median = (s + e) // 2
    if a[s] > a[median]:
        a[median], a[s] = a[s], a[median]
    if a[s] > a[e]:
        a[s], a[e] = a[e], a[s]
    if a[e] < a[median]:
        a[e], a[median] = a[median], a[e]
    a[s + 1], a[median] = a[median], a[s+1]
    return a[median]

def QuickSort3(myList, start, end):
    """
    优化3： 采用三数中值分割法，确定枢纽元
    参考 https://www.cnblogs.com/chengxiao/p/6262208.html
    """
    pass

MINSIZE = 10

def QuickSort4(mylist, start, end):
    """
    优化4：由于快速排序不适用于少量数据，因此当数据量比较少时，采用插入排序
    """
    if start + MINSIZE < end:
        i = start
        j = end
        base = mylist[start]
        while i<j:
            while i<j and (mylist[j] >= base):
                j -= 1
            mylist[i] = mylist[j]
            while i<j and (mylist[i] <= base):
                i += 1
            mylist[j] = mylist[i]

        mylist[i] = base
        QuickSort4(mylist, start, i-1)
        QuickSort4(mylist, i+1, end)
    else:
        insertionSort(mylist)

def insertionSort(mylist):
    for i in range(1, len(mylist)):
        temp = mylist[i]
        j = i
        while j > 0 and (temp < mylist[j-1]):
            mylist[j] = mylist[j-1]
            j -= 1
        mylist[j] = temp


# a = [6,4,3,5,2,0,1]
a = random.sample(range(100), 100)
QuickSort4(a, 0, len(a)-1)
# quickSort(a, 0, len(a)-1)
print(a)

