# -*- coding:utf-8 -*-

"""
二叉查找数
    要求：
    - 树的左节点必须小于右节点
"""

class Node:
    __slot__ = ["value", "left", "right"]

    def __init__(self, value, left, right):
        self.value = value
        self.left =left
        self.right = right


class BinarySearchTree:

    _theSize = 0
    _theRoot = None

    def __init__(self):
        self.clear()

    def clear(self):
        _theRoot = None

    @property
    def getSize(self):
        return self._theSize

    def _find(self, x, node:Node) -> Node:
        if node == None:
            return None

        if node.value > x:
            return self._find(x, node.left)
        elif node.value < x:
            return self._find(x, node.right)
        else:
            return node

    def find(self, x):
        return self._find(x, self._theRoot)

    def contain(self, x):
        return False if  self.find(x) == None else True

    def _insert(self, x, node:Node) -> Node:
        if node == None:
            return Node(x, None, None)

        if x < node.value:
            node.left = self._insert(x, node.left)
        elif x > node.value:
            node.right = self._insert(x, node.right)
        else:
            pass

        return node

    def insert(self, x):
        self._theRoot = self._insert(x, self._theRoot)

    def _listAll(self, node:Node):
        if node == None:
            return

        if node.left != None:
            self._listAll(node.left)
        print(node.value)
        if node.right != None:
            self._listAll(node.right)


    def listAll(self):
        self._listAll(self._theRoot)

    def _findmax(self, node:Node)->Node:
        if node == None:
            return None

        if node.right != None:
            return self._findmax(node.right)
        else:
            return node.value

    def _findmin(self, node:Node)->int:
        if node == None:
            return None

        if node.left != None:
            return self._findmax(node.left)
        else:
            return node.value

    def findmax(self):
        return self._findmax(self._theRoot)

    def findmin(self):
        return self._findmin(self._theRoot)

    def _remove(self, x, node:Node)->Node:
        if node ==None:
            return node

        if x < node.value:
            node.left = self._remove(x, node.left)
        elif x > node.value:
            node.right = self._remove(x, node.right)
        elif node.left != None and node.right != None:
            # 寻找右节点中最小的数替换到当前位置
            node.value = self._findmin(node.right)
            node.right = self._remove(x, node.right)
        else:
            # 右节点可能有值，也可能为空，但是效果都一样的
            node = node.left if node.left != None else node.right
        return node

    def remove(self, x):
        self._theRoot = self._remove(x, self._theRoot)

bst = BinarySearchTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(6)
bst.insert(121)
bst.insert(0)
bst.listAll()
print(bst.find(3).value)
print(bst.find(-1))
print(bst.contain(3))
print(bst.contain(-1))
print(bst._findmax(bst._theRoot))
print(bst._findmin(bst._theRoot))
bst.remove(121)
bst.remove(3)
bst.listAll()
