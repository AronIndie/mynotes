# -*- coding:utf-8 -*-


def get_dis(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def get_min_dis(init, locations):
    n = len(locations)
    arr = [[-1] * n] * 2**n
    s = [0] * n
    print(foo(s, -1, arr, locations, init))


def foo(s, i, arr, locations, init):
    if i == -1:
        pass
    else:
        num = int("".join(list(map(str, s))), 2)
        if arr[num][i] != -1:
            return arr[num][i]
    _min = 1e7
    if min(s) == 1:
        return get_dis(locations[i], init)
    for j, c in enumerate(s):
        if c == 0:
            temp = s[:]
            temp[j] = 1
            if i != -1:
                res = foo(temp, j, arr, locations, init) + get_dis(locations[i], locations[j])
            else:
                res = foo(temp, j, arr, locations, init) + get_dis(init, locations[j])
            if res < _min:
                _min = res
    return _min


if __name__ == '__main__':
    locations = [(2, 2), (2, 8), (6, 6)]
    init = (0, 0)
    get_min_dis(init, locations)