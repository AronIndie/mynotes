# -*- coding:utf-8 -*-

"""

小B正在头疼的一个问题是，给定一个由"("、")"和"?"构成的序列，如何将其中的"?"替换为单个的括号，从而使得该序列成为一个正则序列。
更麻烦的事情在于，替换每个"?"都有着不同的代价，如何才能花费最小的代价将给定的序列转换为一个正则序列。作为朋友，小B希望你能够帮到她。
"""

def foo(string, cost1: list, cost2: list):
    if string == "":
        return 0
    l = len(string)
    if string[0] == "(":
        return foo(string[2:], cost1[1:], cost2[1:]) + cost2[0] # 第一个？取右括号时
    else:
        # 第一个？取左括号时，必须是其后第一个、第三个、第五个...与其配对
        left = cost1[0]
        res = []
        for i in range(1, l, 2):
            if string[i] != ")":
                if i == 1:
                    res.append(left + cost2[1] + foo(string[2:], cost1[2:], cost2[2:]))
                else:
                    a = foo(string[1: i], cost1[1:i], cost2[1:i])
                    b = foo(string[i+1:], cost1[i+1:], cost2[i+1:])
                    res.append(left+ cost2[i] + a + b)
            else:
                res.append(left + foo(string[1:i], cost1[1:i], cost2[1:i]))

        return min(res)


if __name__ == '__main__':
    s = "(????)"
    # 9
    cost1 = [2,1,3,4]
    cost2 = [1,2,5,2]
    print(foo(s, cost1, cost2))