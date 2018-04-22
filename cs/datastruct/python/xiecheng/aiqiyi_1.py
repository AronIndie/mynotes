# -*- coding:utf-8 -*-


def foo(arr):
    if arr[0] == arr[1]:
        for i, a in enumerate(arr):
            if i > 1:
                if a != arr[0]:
                    return i
    else:
        if arr[0] == arr[2]:
            return 1
        if arr[1] == arr[2]:
            return 0


if __name__ == '__main__':
    # print(foo([2,3,3]))
    # print("12345")
    import sys
    while 1:
        a = sys.stdin.read(2)
        print a