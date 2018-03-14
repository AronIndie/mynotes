def guess(x):
    if x < 6:return -1
    if x > 6:return 1
    return 0

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """

    l = 0
    r = n

    while l <= n:
        x = (l + r) // 2
        g = guess(x)
        if g < 0:
            l = x
        elif g > 0:
            r = x

        if g == 0:
            return x

if __name__ == '__main__':
    guessNumber(10)