class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not tin:
            return None

        if len(tin) == 1:
            return TreeNode(tin[0])

        for num1 in pre:
            if num1 in tin:
                break
        node = TreeNode(num1)
        j = tin.index(num1)
        node.left = self.reConstructBinaryTree(pre, tin[:j])
        node.right = self.reConstructBinaryTree(pre, tin[j + 1:])
        return node

if __name__ == '__main__':
    pre, tin = [1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
    a = Solution()
    a.reConstructBinaryTree(pre, tin)