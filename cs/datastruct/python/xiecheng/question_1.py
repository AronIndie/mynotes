# -*- coding:utf-8 -*-


def foo(m, string):
    edges = []
    for _s in string:
        for j, s in enumerate(_s):
            if j % 2 == 0 and j < len(_s)-2:
                edges.append((_s[j], _s[j+2], int(_s[j+1])))
                #dic[_s[j]] = (_s[j+2], int(_s[j+1]))
    return count2(edges[2], edges) + edges[2][2]

def find(edges, i):
    for j in edges:
        if j[0] == i:
            return j
    return None

def count(edges):
    _max = 0
    for i in edges:
        s = set()
        _max1 = 0
        while 1:
            start = i[0]
            end = i[1]
            s.add(start)
            s.add(end)
            _max1 += i[2]
            if _max1 > _max:
                _max = _max1
            _next = find(edges, end)
            if _next:
                if _next[1] in s:
                    return -1
                else:
                    s.add(_next[1])
                    i = _next
            else:
                break
    return _max

def find2(edges, i):
    res = []
    for j in edges:
        if j[0] == i:
            res.append(j)
    return res

def count2(start, edges):
    res = find2(edges, start[1])
    if not res:
        return 0

    s = []
    for i in res:
        s.append(count2(i, edges) + i[2])
    return max(s)








if __name__ == '__main__':
    m = 4
    s = ["A2B3D","A4C2E","A5D", "C3B"]
    print foo(m, s)
