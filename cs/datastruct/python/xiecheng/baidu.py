# -*- coding:utf-8 -*-


def foo(n):
    arr = [5 for i in range(n)]
    s = 1
    part_count = 0
    while max(arr) > 0:
        for i, a in enumerate(arr):
            if a == 5:
                s *= 5 * 4
                arr[i] = 3
                part_count += 1
            elif a == 3:
                s *= (3 * 2)
                arr[i] = 0
                part_count += 1
    # for i in range(1, part_count+1):
    #     s *= i
    return s

_max = 0
def foo2(_map, i, j, path):
    global _max
    if _map[i-1][j-1] > _max:
        _max = _map[i-1][j-1]

    n = len(_map)
    m = len(_map[0])

    count = 0

    if i-1 >= 1 and _map[i-2][j-1] >= _map[i-1][j-1] and (i-1, j) not in path:
        count += 1
        foo2(_map, i-1, j, path + [(i-1, j)])

    if i + 1 <= n and _map[i][j-1] >= _map[i-1][j-1] and (i + 1, j) not in path:
        count += 1
        foo2(_map, i + 1, j, path + [(i + 1, j)])

    if j - 1 >= 1 and _map[i-1][j-2] >= _map[i-1][j-1] and (i, j - 1) not in path:
        count+=1
        foo2(_map, i, j - 1, path + [(i, j - 1)])

    if j + 1 <= m and _map[i-1][j] >= _map[i-1][j-1] and (i, j+1) not in path:
        count+=1
        foo2(_map, i, j+1, path + [(i, j+1)])
    if count == 0:
        return


if __name__ == '__main__':
    print(foo(3))
    _map = [[1,5,2], [0, 4,9]]
    i, j = 1, 1
    _path = [(1, 1)]
    foo2(_map, i, j, _path)
    print(_max)

