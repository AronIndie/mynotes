# -*- coding:utf-8 -*-

"""
输入： 一组数组，第一行a,b,c，表示后面有多少行，卡片的长和宽
后面每一行m,n表示信封的长和宽
输出：最多多少个信封可以一层套一层套住这些卡片，并且输出信封编号（一样的大的信封取靠前的）
"""


_res = []
def foo(lst, init):
    if init[0] >= max(list(zip(*lst))[0]) or init[1] >= max(list(zip(*lst))[1]):
        return 0

    temp = []
    for i in lst:
        if i[0] > init[0] and i[1] > init[1]:
            temp.append(i)

    if not temp:
        return foo(lst, [i+1 for i in init])
    else:
        res = []
        for i in temp:
            res.append(foo(lst, i))
        if max(res) != 0:
            a = temp[res.index(max(res))]
            if a not in _res:
                _res.append(a)
        else:
            if temp[0] not in _res:
                _res.append(temp[0])
        return max(res) + 1

import sys
const_n = 0
const_v = 1
const_p = 2


def main():
    while True:
        line = list(map(int, sys.stdin.readline().strip().split()))
        n, vm = line[0], line[1]

        candies = []
        for i in range(n):
            line = list(map(int, sys.stdin.readline().strip().split()))
            if len(line) < 2:
                break
            candies.append((i + 1, line[0], line[1]))

        candies = sorted(candies, key=lambda s: float(s[const_p]) / float(s[const_v]), reverse=True)
        # print candies

        seq = set([])
        v = p = 0
        l = r = -1
        for i, candy in enumerate(candies):
            if v + candy[const_v] >= vm:
                if v + candy[const_v] == vm:
                    seq.add(candy[const_n])
                    p += candy[const_p]
                else:
                    for j in range(i + 1, n):
                        if candies[j][const_v] == 1:
                            r = j
                            break

                    if l == -1 and r == -1:
                        pass
                    elif l == -1 and r != -1:
                        p += candies[r][const_p]
                        seq.add(candies[r][const_n])
                    elif l != -1 and r == -1:
                        if candy[const_p] - candies[l][const_p] > 0:
                            p = p - candies[l][const_p] + candy[const_p]
                            seq.remove(candies[l][const_n])
                            seq.add(candy[const_n])
                    else:
                        if candy[const_p] - candies[l][const_p] > candies[r][const_p]:
                            p = p - candies[l][const_p] + candy[const_p]
                            seq.remove(candies[l][const_n])
                            seq.add(candy[const_n])
                        else:
                            p += candies[r][const_p]
                            seq.add(candies[r][const_n])
                break

            seq.add(candy[const_n])
            v += candy[const_v]
            p += candy[const_p]

            if candy[const_v] == 1:
                l = i

        print(p)
        if p > 0:
            seq = sorted(seq)
            for s in seq:
                print(s,)
        else:
            print('No')
        print()

if __name__ == '__main__':
    lst = [(5,3), (12, 11), (9, 8),(13,12), (14,14)]
    lst = [(2,2), (2,2)]
    init = (1,1)
    print(foo(lst, init))
    _res.reverse()

    print([lst.index(x)+1 for x in _res])