# -*- coding:utf-8 -*-

"""
根据所给元素生成霍夫曼树
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


dic = {}
def gen_hoffman_tree(arr):
    if len(arr) < 2:
        return
    arr.sort()
    a = arr.pop(0)
    b = arr.pop(0)
    node = Node(a+b)
    if a in dic:
        node.left = dic[a]
    if b in dic:
        node.right = dic[b]
    if not arr:
        return node

    dic[a+b] = node
    arr.append(a+b)
    return gen_hoffman_tree(arr)

if __name__ == '__main__':
    arr = [1,3,5,6,7,8]
    for i in arr:
        dic[i] = Node(i)
    a = gen_hoffman_tree(arr)
    print(a)