# -*- coding:utf-8 -*-


def foo(arr):
    l_max = [arr[0]]
    l_min = [arr[0]]
    for i in arr:
        l_max.append(max(max(i*l_max[-1], i*l_min[-1]), i))
        l_min.append(min(min(i*l_max[-1], i*l_min[-1]), i))
    return max(l_max+l_min)


if __name__ == '__main__':
    print(foo([1,2,-3,-2,0,1,4]))
