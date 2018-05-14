# -*- coding:utf-8 -*-


"""
Leetcode 22. https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""


def foo(num):
    """
    方法：
    1. 加左括号
    2. 加右括号

    条件：
    1. 当左括号有剩余时，加左括号
    2. 当左括号数目大于右括号时（还剩的右括号数目大于左括号），加右括号
    """

    res = []
    backtrace("", res, num, num)
    return res


def backtrace(sub, res, left, right):
    if left == 0 and right == 0:
        res.append(sub)
    if left > 0:
        backtrace(sub+"(", res, left-1, right)
    if right > left:
        backtrace(sub+")", res, left, right-1)


if __name__ == "__main__":
    print(foo(3))
