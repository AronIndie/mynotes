# -*- coding:utf-8 -*-

"""
最长无连续子串
"""

def foo(s: str) -> str:
    i, j = 0, 0
    _set = set()
    _set.add(s[0])
    _max = ""
    while j < len(s)-1:
        j += 1
        if s[j] not in _set:
            _set.add(s[j])
        else:
            temp = s[i:j]
            if len(temp) > len(_max):
                _max = temp
            while s[i] != s[j]:
                i += 1
            i += 1
    if len(_max) < len(s[i:]):
        _max = s[i:]
    return _max

"""
全排列问题
"""
res = []
def all_range(arr, i):
    if i == len(arr) - 1:
        res.append(arr[:])
    else:
        for j in range(i, len(arr)):
            swap(arr, i, j)
            all_range(arr, i + 1)
            swap(arr, i, j)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



def quick_sort(arr, i, j):
    if i >= j:
        return
    flag = arr[j]
    left = i
    right = j
    while i < j:
        while i < j and arr[i] <= flag:
            i += 1
        arr[j] = arr[i]
        while i < j and arr[j] > flag:
            j -= 1
        arr[i] = arr[j]

    arr[i] = flag
    quick_sort(arr, left, i-1)
    quick_sort(arr, i+1, right)



if __name__ == '__main__':
    print(foo("babcdcefgh"))
    all_range([1,2,3], 0)
    print(res)
    a = [5,3,1,6,8,9, 7]
    quick_sort(a, 0, len(a)- 1)
    print(a)