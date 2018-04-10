# -*- coding:utf-8 -*-


def drop_ball(height):
    res = -height
    while height > 0:
        res += 2 * height
        height = height / 2
    return res

if __name__ == '__main__':
    print(drop_ball(100) + drop_ball(90)+drop_ball(80)+drop_ball(70))
    print(drop_ball(100))