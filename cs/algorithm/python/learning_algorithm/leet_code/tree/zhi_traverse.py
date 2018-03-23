class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        # two stack
        if not pRoot:
            return []

        s1 = []
        s2 = [pRoot]
        res = []
        while s1 or s2:
            t = []
            while s2:
                temp = s2.pop()
                t.append(temp)
                if temp.left:
                    s1.append(temp.left)
                if temp.right:
                    s1.append(temp.right)
            res.append(t)
            t = []
            while s1:
                temp = s1.pop()
                t.append(temp)
                if temp.right:
                    s2.append(temp.right)
                if temp.left:
                    s2.append(temp.left)
            res.append(t)
        return res

if __name__ == '__main__':
    from leet_code.tree.gen_tree_from_list import *
    t = gen_tree([8,6,10,5,7,9,11])
    s = Solution()
    s.Print(t)