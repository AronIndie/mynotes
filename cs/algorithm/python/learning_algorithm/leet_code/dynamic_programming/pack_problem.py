# -*- coding:utf-8 -*-


class Solution:

    def pack_0_1(self, W: list, V: list, C: int):
        """
        如果不需要输出路径，可以用一个一维数组替代arr
        """
        if not W or C == 0:
            return 0

        arr = [[0 for i in range(C + 1)] for j in range(len(W))]
        selected = []
        for i, w in enumerate(W):
            for j in range(1, C+1):
                if j < w:
                    arr[i][j] = arr[i-1][j]
                else:
                    if i > 0:
                        a, b = arr[i-1][j], arr[i-1][j-w] + V[i]
                        arr[i][j] = max(a, b)
                    else:
                        arr[i][j] = V[i]

        init = C
        for i in range(1, len(arr)):
            if arr[i][init] ==  arr[i-1][init]:
                selected.append(0)
            else:
                selected.append(1)
                init -= W[i]
        if init > 0:
            selected.append(1)
        else:
            selected.append(0)

        return arr[-1][C], selected

    def pack_infinity(self, W, V, C):
        if not W or C == 0:
            return 0

        arr = [[0 for i in range(C + 1)] for j in range(len(W))]
        selected = []
        for i, w in enumerate(W):
            for j in range(1, C + 1):
                if i > 0:
                    a = arr[i - 1][j]
                    if j >= w:
                        b = arr[i][j - w] + V[i]
                        arr[i][j] = max(a, b)
                    else:
                        arr[i][j] = a
                else:
                    if j >= w:
                        arr[i][j] = arr[i][j -w] + V[i]
                    else:
                        arr[i][j] = 0

        return arr[-1][C]

    def pack_multiply(self, W, V, A, C):
        """
        多重背包问题，每个item给定一定的数目
        方案一：每次内部对数目count进行循环（有问题）
        方案二：拆分成0-1问题

        """
        if not W or C == 0:
            return 0

        arr = [[0 for i in range(C + 1)] for j in range(len(W))]
        selected = []
        for i, w in enumerate(W):
            for j in range(1, C + 1):
                if i > 0:
                    a = arr[i - 1][j]
                    if j >= w:
                        count = min(A[i], j // w)
                        for k in range(1, count+1):
                            temp = arr[i][j - k*w] + k*V[i]
                            if temp > arr[i][j]:
                                arr[i][j] = temp
                        arr[i][j] = max(a, arr[i][j])
                    else:
                        arr[i][j] = a
                else:
                    if j >= w:
                        count = min(A[i], j // w)
                        for k in range(1, count+1):
                            temp = arr[i][j - k*w] + k*V[i]
                            if temp > arr[i][j]:
                                arr[i][j] = temp
                    else:
                        arr[i][j] = 0
        return arr[-1][C]


if __name__ == '__main__':
    W = [2, 2, 6, 5, 4]
    V = [6, 3, 5, 4, 6]
    C = 10
    s = Solution()
    #print(s.pack_0_1(W, V, C))
    W2 = [2, 3, 4, 7]
    V2 = [1, 3, 5, 9]
    C = 10
    #print(s.pack_infinity(W2, V2, C))
    W3 = [1,2,2]
    V3 = [6,10,10]
    A3 = [10,5,2]
    C = 12
    print(s.pack_multiply(W3, V3, A3, C))


