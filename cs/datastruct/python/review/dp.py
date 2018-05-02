# -*- coding:utf-8 -*-


def full_range(arr, i):
    global res
    if i >= len(arr) - 1:
        res.append(arr[:])
    else:

        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            full_range(arr, i+1)
            arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = [1,2,3]
    res = []
    full_range(arr, 0)
    print(res)
