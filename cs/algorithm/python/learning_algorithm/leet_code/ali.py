# -*- coding:utf-8 -*-

M=5
N=5
# Sn = -Sn-1 + m*(m-1)^(n-1)

def total(m, n):
    if n == 2:
        return m * (m - 1)

    return m * (m-1)**(n-1) - total(m, n-1)

print(total(3, 3))