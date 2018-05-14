# -*- coding:utf-8 -*-

import numpy as np
"""
leetcode 51. https://leetcode.com/problems/n-queens/description/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
"""

def backtrace(sub, mat, res, row):
    if row >= mat.shape[0]:
        res.append(sub[:])

    for i in range(mat.shape[0]):
        if legal(mat, row, i):
            mat[row, i] = 1
            s = ["."] * mat.shape[0]
            s[i] = 'Q'
            sub.append(''.join(s))
            backtrace(sub, mat, res, row+1)
            sub.pop()
            mat[row, i] = 0


def legal(mat, row, i):
    if row == 0:
        return True
    for j in range(mat.shape[0]):
        for k in range(mat.shape[1]):
            if mat[j, k] == 1:
                if row == j or i == k:
                    return False
                if abs(row-j) == abs(i-k):
                    return False
    return True


def foo(n):
    sub =[]
    mat = np.zeros((n, n))
    res = []
    backtrace(sub, mat, res, 0)
    return res


def test_legal():
    mat = np.zeros((4, 4))
    mat[0,1] = 1
    print(legal(mat, 1, 3))


# 更优方法

class Solution(object):
    def solveNQueens(self, n):

        self.res = []
        self.n = n
        self.dfs([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in self.res]

    def dfs(self, queens, xy_dif, xy_sum):
        p = len(queens)
        if p == self.n:
            self.res.append(queens)
            return
        for q in range(self.n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                self.dfs(queens + [q], xy_dif + [p - q], xy_sum + [p + q])


if __name__ == '__main__':
    test_legal()
    print(foo(4))
    s = Solution()
    s.solveNQueens(4)