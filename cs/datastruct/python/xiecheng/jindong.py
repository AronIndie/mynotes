# -*- coding:utf-8 -*-


def foo(num):
    if num % 2 == 1:
        return "No"

    n = num // 2
    res = -1
    for i in range(1, n):
        k = 2**i
        if k > num:
            break
        if num % k != 0:
            continue
        j = num // k
        if j % 2 == 1:
            res = j
            break
    if res == -1:
        return "No"
    return "%s %s" % (res, num // res)

dic = {}
dic2 = set()
def foo2(s, i, j):
    if (i, j) in dic and i != j:
        return dic[(i, j)]
    if i == j:
        if i in dic2:
            res = 0
        else:
            dic2.add(i)
            res = 1
    elif j - i == 1:
        res = foo2(s, i, j-1) + foo2(s, i+1, j)
    else:
        if s[i] == s[j]:
            res = foo2(s, i+1, j-1) + foo2(s, i+1, j) + foo2(s, i, j-1) + 2
        else:
            res =  foo2(s, i+1, j) + foo2(s, i, j-1)
    dic[(i, j)] = res
    return res


def foo3(k, x, y):
    if k == 0:
        if x == 1 and y == 1:
            return 1
        return 0

    if x - 1 > 0 and y - 2 > 0:
        a = foo3(k-1, x-1, y-2)
    if x - 1 > 0 and y + 2 <= 8:
        b = foo3(k-1, x-1, y+2)
    if x + 1 <= 8 and y-2 > 0:
        c = foo3(k-1, x+1, y-2)


def foo4(k, x, y):
    k_list = []

    for i in range(k+1):
        x_y = [[0 for j in range(9)] for w in range(9)]
        if i == 0:
            x_y[0][0] = 1
        else:
            for m in range(9):
                for n in range(9):
                    s = 0
                    if m - 2 >= 0 and n - 1 >= 0:
                        s += k_list[-1][m-2][n-1]
                    if m - 1 >= 0 and n - 2 >= 0:
                        s += k_list[-1][m-1][n-2]
                    if m - 2 >= 0 and n + 1 <= 8:
                        s += k_list[-1][m-2][n+1]
                    if m - 1 >= 0 and n + 2 <= 8:
                        s += k_list[-1][m-1][n+2]
                    if m + 2 <= 8 and n - 1 >= 0:
                        s += k_list[-1][m + 2][n - 1]
                    if m + 1 <= 8 and n - 2 >= 0:
                        s += k_list[-1][m + 1][n - 2]
                    if m + 2 <= 8 and n + 1 <= 8:
                        s += k_list[-1][m + 2][n + 1]
                    if m + 1 <=8 and n + 2 <= 8:
                        s += k_list[-1][m + 1][n + 2]
                    x_y[m][n] += s
        k_list.append(x_y)
    return k_list[-1][x][y]

if __name__ == '__main__':
    # print(foo(200))
    # print(foo2("ABAC", 0, 3))
    print(foo4(2, 3, 3))