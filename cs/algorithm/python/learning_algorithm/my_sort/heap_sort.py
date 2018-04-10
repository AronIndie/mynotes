# -*- coding:utf-8 -*-


"""
ref: https://www.cnblogs.com/chengxiao/p/6129630.html

记住：
非叶子节点的数目 = len(heap) // 2 - 1
给定非叶子节点i，其子节点索引为 2*i +1 和 2*i+2
"""


def heap_sort(a: list):
    for i in range(len(a) - 1, -1, -1):
        # 从第一个非叶子节点，从上至下，从右至左调整
        a = adj_small_heap(a, i)

    for j in range(len(a) - 1, 0, -1):
        a[0], a[j] = a[j], a[0]
        a[:j] = adj_small_heap(a[:j], 0)
    return a


def adj_heap(a, i):
    """
    调整数组使其满足堆的性质（大顶堆）
    :param a: 数组
    :param i: 第i个叶子节点
    :return: void
    """
    temp = a[i]
    k = 2 * i + 1
    while k < len(a):
        # 判断右节点和左节点那个大，如果右节点更大，则把k指向其
        if k + 1 < len(a) and a[k + 1] > a[k]:
            k += 1

        # 如果子节点值更小，则下沉，不用交换，类似插入排序
        if temp < a[k]:
            a[i] = a[k]
            i = k
        else:
            break
        k = 2 * k + 1
    a[i] = temp
    return a

def adj_small_heap(a, i):
    """
    调整数组使其满足堆的性质（小顶堆）
    :param a: 数组
    :param i: 第i个叶子节点
    :return: void
    """
    temp = a[i]
    k = 2 * i + 1
    while k < len(a):
        # 判断右节点和左节点那个大，如果右节点更大，则把k指向其
        if k + 1 < len(a) and a[k + 1] < a[k]:
            k += 1

        # 如果子节点值更小，则下沉，不用交换，类似插入排序
        if temp > a[k]:
            a[i] = a[k]
            i = k
        else:
            break
        k = 2 * k + 1
    a[i] = temp
    return a

if __name__ == '__main__':
    a = [1,3,2,6,5,4]
    print(heap_sort(a))