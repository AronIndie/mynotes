# -*- coding:utf-8 -*-


"""
输入：
- 地牢形状 . 表示可通行 X 表示不可通行
- 开始坐标： x0, y0，结束坐标为地牢右下角
- 合法的步长列表 [(0,1), (1,0), (-2, 0)] 表示只能往下走1个单位，或者往右走一个单位，或者往左走一个单位
"""


res = []

def foo(n, m, shape_list, start, legal_step):
    global res
    backtrace(n, m, shape_list, 0, legal_step, start)
    return min(res)


def backtrace(n, m, shape_list: list, step_count: int, legal_step: list, start: tuple):
    global res
    if start[0] >= n or start[1] >= m or shape_list[start[1]][start[0]] == "X":
        return


    if start[0] == n-1 and start[1] == m-1:
        res.append(step_count)

    for step in legal_step:
        end = (start[0] + step[0], start[1] + step[1])

        backtrace(n,m,shape_list,step_count+1,legal_step, end)


if __name__ == '__main__':
    print(foo(4, 3, [["."]*4]*3, (0,0), [(1, 0), (0, 2)]))


