# -*- coding:utf-8 -*-


def find(left, n):
    res = []
    for i,pair in enumerate(left):
        if pair == n:
            res.append(i)
    return res

def foo(root, left, right, target):
    queue = [root]
    s = set()
    res = -1
    while queue:
        temp = queue.pop(0)
        if tuple(temp) not in s:
            s.add(tuple(temp))
        else:
            return -1
        if temp[0] == target and res == -1:
            res = temp[1]
        idx = find(left, temp)
        for i in idx:
            queue.append(right[i])
    return res


operator = {"+", "-", "*"}
operator2 = {"(", ")"}
def parse_error(s):
    res = []
    temp = []
    for i in s:
        if str.isdigit(i):
            if len(res) > 0 and res[-1] == " ":
                return "Error"
            temp.append(i)
        else:
            res.append(int("".join(temp)))
            if i == " ":
                if len(res) > 0 and isinstance(res[-1], int):
                    res.append(" ")
                else:
                    pass
            elif i in operator:
                if len(res) > 0 and (isinstance(res[-1], int) or res[-1] == ")"):
                    res.append(i)
                else:
                    return "Error"
            elif i in operator2:
                if i == "(":
                    if len(res) > 1 and isinstance(res[-1], int):
                        return "Error"
                    res.append("(")
                elif i == ")":
                    if len(res) > 1 and isinstance(res[-1], int):
                        res.append(")")
                    return "Error"
    if temp:
        res.append(int("".join(temp)))
    return res

def parse(s):
    s = s.replace(" ", "")
    res = []
    temp = []
    for i in s:
        if str.isdigit(i):
            temp.append(i)
        else:
            if temp:
                res.append(int("".join(temp)))
            temp = []
            res.append(i)
    if temp:
        res.append(int("".join(temp)))
    return res

dic = {"(":3, ")":3, "+":2, "-":2, "*":1}
def transfer(arr):
    stack = []
    postfix = []
    for i in arr:
        if isinstance(i, int):
            postfix.append(i)
        else:
            if i == ")":
                while stack[-1] != "(":
                    postfix.append(stack.pop())
                stack.pop()
            else:
                if stack:
                    while dic[i] <= dic[stack[-1]] and stack[-1] != "(":
                        postfix.append(stack.pop())
                        if not stack:
                            break
                stack.append(i)
    while stack:
        postfix.append(stack.pop())
    return postfix

def calculate(postfix):
    stack = []
    for i in postfix:
        if isinstance(i, int):
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            c = 0
            if i == "+":
                c = a+b
            elif i == "-":
                c = b - a
            elif i == "*":
                c = b * a
            stack.append(c)
    return stack[-1]

if __name__ == '__main__':
    target = "e"
    root = ["a", "1"]
    left = [["b", "1"], ["c", "1"], ["a", "1"], ["a", "1"], ["a", "1"]]
    right = [["e", "2"], ["a", "1"], ["b", "1"], ["c", "1"], ["d", "1"]]
    #print(foo(root, left, right, target))

    a = "1 + 2 * 3 - (4*5)"
    arr = parse(a)

    pst = transfer(arr)
    print(calculate(pst))
