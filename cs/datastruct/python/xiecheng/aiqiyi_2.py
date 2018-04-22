# -*- coding:utf-8 -*-

def foo(arr):
    arr.sort()

    a = arr[0] % 2
    b = arr[1] % 2
    c = arr[2] % 2

    if b == c:
        if a == b:
            return (arr[2] - arr[1]) / 2 + (arr[2] - arr[0]) / 2
        else:
            return (arr[2] - arr[1]) / 2 + (arr[2] + 1 - arr[0]) / 2 + 1
    else:
        arr[0] += 1
        arr[1] += 1
        return foo(arr)





if __name__ == '__main__':
    print(foo([12, 10,1 ]))

