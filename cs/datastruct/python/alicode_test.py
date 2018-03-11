# -*- coding:utf-8 -*-


class node:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class Solution:

    def twoSum(self, arr, target):
        res = []
        s = set()
        for i, num in enumerate(arr):
            # 在arr排序的情况下
            diff = target - num
            if diff in s:
                temp = [num, diff]
                temp.sort()
                res.append(tuple(temp))
            s.add(num)
        return list(set(res))

    def threeSum(self, arr):
        arr.sort()
        res = []
        length = len(arr)
        if length < 3:
            return res

        for i, num in enumerate(arr):
            if num > 0:
                return res
            if i > 0 and arr[i-1] == num:
                continue
            if i > length-3:
                break

            two_sum_res = self.twoSum(arr[i+1:], -arr[i])
            print(two_sum_res)
            for pair in two_sum_res:
                pair = list(pair)
                pair.insert(0, num)
                res.append(tuple(pair))
        return list(set(res))


if __name__ == '__main__':
    a = Solution()

    #rint(a.twoSum([0,0,0,-1], -1))
    print(a.threeSum([-1,0,1,2,-1,-4]))

