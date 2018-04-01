# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        queue = [pRoot]
        row_count = 1
        res = []
        while queue:
            count = 0
            next_row_count = 0
            row_res = []
            while count < row_count:
                temp = queue.pop(0)
                row_res.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                    next_row_count += 1
                if temp.right:
                    queue.append(temp.right)
                    next_row_count += 1
                count += 1
            res.append(row_res)
            row_count = next_row_count
            if row_count == 0:
                break
        return res

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
    print(s.Print(node1))
