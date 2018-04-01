# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        if not root:
            return "#,"

        left = self.Serialize(root.left)
        right = self.Serialize(root.right)
        return str(root.val) + "," + left + right

    flag = -1
    def Deserialize(self, s):
        self.flag += 1
        l = s.split(',')
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '#'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    s = Solution()
    s1 = s.Serialize(node1)
    print(s1)
    root = s.Deserialize(s1)
    pass