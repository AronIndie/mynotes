# -*- coding:utf-8 -*-

"""
已知前序和中序遍历推导后序遍历
"""

def get_post_order(pre_order, in_order, res):
    if not in_order:
        return
    temp = 0
    for i in pre_order:
        if i in in_order:
            temp = in_order.index(i)
            break
    res.append(in_order[temp])
    get_post_order(pre_order, in_order[temp+1:], res)
    get_post_order(pre_order, in_order[:temp], res)

if __name__ == '__main__':
    a = [4,2,1,3,7,5,6,8]
    b = [1,2,3,4,5,6,7,8]
    res = []
    get_post_order(a, b, res)
    res.reverse()
    print(res)