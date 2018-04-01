# -*- coding:utf-8 -*-

"""
剑指offer，矩阵中的路径

"""
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        matrix = list(matrix)
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.find(matrix, rows, cols, path[1:], i, j):
                        return True
        return False

    def find2(self, matrix, rows, cols, path, i, j):
        if path == "":
            return True

        matrix[i * cols + j] = ''
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j+1)
        if j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j-1)
        if i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i+1, j)
        if i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i-1, j)
        return False

    def find(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i * cols + j] = '0'
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i, j - 1)
        elif i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.find(matrix, rows, cols, path[1:], i - 1, j)
        else:
            return False

if __name__ == '__main__':
    # 有问题啊这一题
    matrix = "ABCESFCEADEE"
    row, col = 3,4
    path = "ABCCED"
    s = Solution()
    print(s.hasPath(matrix, row, col, path))