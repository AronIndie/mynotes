# -*- coding:utf-8 -*-


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def gen_tree(arr):
    if len(arr) == 0:
        return None
    nodes = [Node(i) if i != "#" else None for i in arr]
    for i in range(len(nodes) // 2 - 1, -1, -1):
        k = 2 * i + 1
        if k < len(nodes):
            nodes[i].left = nodes[k]
        if k + 1 < len(nodes):
            nodes[i].right = nodes[k+1]
    return nodes[0]


def pre_order_traverse(root):
    if not root:
        return
    print(root.value)
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)


def in_order_traverse(root):
    if not root:
        return
    in_order_traverse(root.left)
    print(root.value)
    in_order_traverse(root.right)


def post_order_traverse(root):
    if not root:
        return
    post_order_traverse(root.left)
    post_order_traverse(root.right)
    print(root.value)


def pre_order_traverse_NC(root):
    stack = [root]
    while stack:
        temp = stack.pop()
        print(temp.value)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


def in_order_traverse_NC(root):
    stack = []
    temp = root
    while temp or stack:
        if temp:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(temp.value)
            temp = temp.right


def post_order_traverse_NC1(root):
    stack1 = [root]
    stack2 = []
    while stack1:
        temp = stack1.pop()
        stack2.append(temp)
        if temp.left:
            stack1.append(temp.left)
        if temp.right:
            stack2.append(temp.right)
    while stack2:
        print(stack2.pop())

def post_order_traverse_NC2(root):
    stack = [root]
    bool_dic = {}
    while stack:
        node = stack[-1]
        if (not node.left and not node.right) or node in bool_dic:
            print(stack.pop().value)

        if node not in bool_dic:
            bool_dic[node] = True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def breadth_first_traverse(root):
    queue = [root]

    while queue:
        temp = queue.pop(0)
        print(temp.value)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9,10]
    theRoot = gen_tree(arr)
    print(post_order_traverse(theRoot))
    # print(pre_order_traverse(root))
    # print(post_order_traverse_NC2(root))
    print(breadth_first_traverse(theRoot))


