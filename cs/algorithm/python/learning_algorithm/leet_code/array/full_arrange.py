# -*- coding:utf-8 -*-

def full_arrange(arr):

    if not arr or len(arr) == 1:
        return [arr]

    res = []
    temp = full_arrange(arr[1:])
    for i in temp:
        for j in range(len(i) + 1):
            res.append(i[:j] + arr[0:1] + i[j:])
    return res

res = []

def full_range(arr, i, j):
    if i == j:
        res.append(arr[:])
    else:
        used = []
        for s in range(i, j+1):
            if arr[s] in used:
                continue
            else:
                used.append(arr[s])
            swap(arr, i, s)
            full_range(arr, i+1, j)
            swap(arr, i, s)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    full_range([1,2,3,3], 0, 3)
    print(res)