# -*- coding:utf-8 -*-

class Soulution:
    def multiply(self, A):

        D = [None for i in range(len(A))]
        C = [None for i in range(len(A))]

        D[0] = 1
        C[-1] = 1

        for i in range(len(A)):
            if not D[i]:
                D[i] = D[i-1] * A[i-1]
            j = len(A) - 1 - i
            if not C[j]:
                C[j] = C[j+1] * A[j + 1]

        res = []
        for i in range(len(A)):
            res.append(D[i] * C[i])

        return res

if __name__ == '__main__':
    a = [1,2,3,4]
    S = Soulution()
    print(S.multiply(a))

