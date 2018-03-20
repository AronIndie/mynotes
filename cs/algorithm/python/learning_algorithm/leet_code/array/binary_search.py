# -*- coding:utf-8 -*-

def b_search(arr, t):
    l = 0
    r = len(arr) - 1

    while l <= r :
        mid = (l + r) // 2
        if t < arr[mid]:
            r = mid - 1
        elif t > arr[mid]:
            l = mid + 1
        else:
            return True
    return False


def Find(target, array):
    # 二维列表搜索
    if len(array) == 0:
        return False
    if len(array[0]) == 0:
        return False

    i = len(array) - 1
    j = 0
    while i > 0 or j < len(array) - 1:
        if target < array[i][j]:
            for p in range(i, -1, -1):
                if array[p][j] <= target:
                    i = p
                    break
            else:
                return False
        elif target > array[i][j]:
            for p in range(j, len(array[0])):
                if target <= array[i][p]:
                    j = p
                    break
            else:
                return False
        else:
            return True
    return False


if __name__ == '__main__':
    a = [1,2,4,6,7,9,10]
    b = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    # print(b_search(a, 3))
    print(Find(0, b))
