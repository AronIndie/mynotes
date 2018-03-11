# -*- coding:utf-8 -*-

import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Cost Time: %.6f" % (end - start))
    return wrapper


@timeit
def time_of_n(n):
    for i in range(n):
        i *= i

if __name__ == '__main__':
    time_of_n(100000)