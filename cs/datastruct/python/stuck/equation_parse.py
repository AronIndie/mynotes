# -*- coding:utf-8 -*-

"""
公式解析，给定文本表达式，计算出结果并且进行检验
"""
from enum import Enum

class Stack(object):
    def __init__(self):
        self._stuck = []

    def clear(self):
        self._stuck = []

    @property
    def length(self):
        return len(self._stuck)

    def push(self, value):
        self._stuck.insert(0, value)

    def pop(self):
        if self.length == 0:
            raise Exception("No element")
        return self._stuck.pop(0)

    def get_first(self):
        if self.length == 0:
            raise Exception("No element")
        return self._stuck[0]

level_dict = {
    "+" : 0,
    "-" : 0,
    "*" : 1,
    "/" : 1,
    "(" : 2,
    ")" : 2,
}

def parse_formula(formula: str):
    """
    formula = '1+2*(3-1)'
    """
    stack = Stack()
    result = ""
    for i in formula:
        if str.isdigit(i):
            result += i
        else:
            if stack.length == 0:
                stack.push(i)
            else:
                if i == ")":
                    while stack.get_first() != "(":
                        result += stack.pop()
                    stack.pop()
                else:
                    while level_dict[stack.get_first()] >= level_dict[i] and stack.get_first() != "(":
                        result += stack.pop()
                        if stack.length == 0:
                            break
                    stack.push(i)
    while stack.length != 0:
        result += stack.pop()
    return result


def calculate(parsed_formula):
    stack = Stack()
    for i in parsed_formula:
        if str.isdigit(i):
            stack.push(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == "*":
                stack.push(a * b)
            elif i == "/":
                stack.push(a / b)
            elif i == "+":
                stack.push(a + b)
            elif i == "-":
                stack.push(a - b)

    return stack.pop()

if __name__ == '__main__':
    parsed = parse_formula('1+2*3+(4*5+6)*7')
    print(calculate(parsed))
