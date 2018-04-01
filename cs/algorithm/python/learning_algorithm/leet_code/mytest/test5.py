# -*- coding:utf-8 -*-



def foo(c, W, V):

    _mat = [[0 for i in range(c+1)] for j in range(len(W))]

    for i, w in enumerate(W):
        for j in range(w, c+1):
            if w > j:
                _mat[i][j] = _mat[i-1][j]
            else:
                if i >= 1:
                    _mat[i][j] = max(_mat[i-1][j], _mat[i-1][j-w] + V[i])
                else:
                    _mat[i][j] = V[i]

    res = []
    init = c
    for i in range(len(_mat)-1, 0, -1):
        if _mat[i][init] > _mat[i-1][init]:
            res.append(i)
            init -= W[i]
    if _mat[0][init] > 0:
        res.append(0)
    res.reverse()
    for i in _mat:
        print(i)
    return _mat[-1][-1], res


print(foo(3, [1,2,1,2,1], [9,9,9,10,6]))

