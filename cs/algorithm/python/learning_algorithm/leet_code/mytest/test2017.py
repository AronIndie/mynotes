# -*- coding:utf-8 -*-


def foo(s):
    l = len(s)
    min = l
    for i in range(l):
        x = []
        for j in 'ABCDE':
            x.append(s.find(j))
        x.sort()
        if min > x[-1]:
            min = x[-1]
        s = s[1:] + s[0]
    print(l - min - 1)



if __name__ == '__main__':
    s = "ATTMBQECPD"
    foo(s)