# -*- coding:utf-8 -*-


"""
有 n 个学生站成一排，每个学生有一个能力值，
从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，
使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
"""

def foo(arr, k, d):
    fm = [[0 for i in range(len(arr))] for j in range(k)]
    fn = [[0 for i in range(len(arr))] for j in range(k)]

    for _k in range(k):
        for _i in range(len(arr)):
            if _k == 0:
                fm[_k][_i], fn[_k][_i] = arr[_i], arr[_i]
            else:
                for j in range(_i-1, max(_i-d, 0)-1, -1):
                    fm[_k][_i] = max(fm[_k][_i], max(fm[_k-1][j]*arr[_i], fn[_k-1][j]*arr[_i]))
                    fn[_k][_i] = min(fn[_k][_i], min(fm[_k-1][j]*arr[_i], fn[_k-1][j]*arr[_i]))
    return fm[-1][-1]


if __name__ == '__main__':
    print(foo([7,3,7], 2, 2))

