# -*- coding:utf-8 -*-


class Node:

    def __init__(self, val, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


def gen_tree(s):
    nodes = [None for i in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        if s[i] != "#":
            nodes[i] = Node(int(s[i]))
            if 2 * i + 1 < len(s):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(s):
                nodes[i].right = nodes[2 * i + 2]
        else:
            nodes[i] = None
    return nodes[0]



def pre_order_traverse(root):

    stack = [root]
    while stack:
        temp = stack.pop()
        print(temp.val)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


def in_order_traverse(root):
    stack = []
    temp = root
    while stack or temp:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(temp.val)
            temp = temp.right


def post_order_traverse1(root):
    stack = [root]
    marked = []
    while stack:
        temp = stack[-1]
        if temp.left is None and temp.right is None:
            print(stack.pop().val)
        elif temp not in marked:
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            marked.append(temp)
        else:
            print(stack.pop().val)


def post_order_traverse2(root):
    stack = [root]
    res = []
    while stack:
        temp = stack.pop()
        res.append(temp.val)
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
    print(res[::-1])


def bfs(root):
    queue = [root]
    while queue:
        temp = queue.pop()
        print(temp.val)
        if temp.left:
            queue.insert(0, temp.left)
        if temp.right:
            queue.insert(0, temp.right)


def rotate_tree(root):

    if not root or (root.left is None and root.right is None):
        return root
    root.left, root.right = rotate_tree(root.right), rotate_tree(root.left)
    return root


def is_mirror_tree(root):
    return is_mirror(root.left, root.right)


def is_mirror(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.val == root2.val:
        return is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)
    return False


if __name__ == "__main__":
    s = "1224554"
    root = gen_tree(s)
    # pre_order_traverse(root)
    # in_order_traverse(root)
    # post_order_traverse1(root)
    # bfs(root)
    # root = rotate_tree(root)
    # bfs(root)
    print(is_mirror_tree(root))
