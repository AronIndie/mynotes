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

if __name__ == '__main__':
    a = full_arrange([1,2,3,4])
    print(a)