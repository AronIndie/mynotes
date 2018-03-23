# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        self.merge_sort(data)
        return self.count

    count = 0

    def merge_sort(self, arr):
        if not arr or len(arr) == 1:
            return arr

        if len(arr) == 2:
            if arr[0] > arr[1]:
                self.count += 1
                arr.reverse()
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, arr1, arr2):
        if not arr1 and not arr2:
            return []
        if not arr1:
            return arr2
        elif not arr2:
            return arr1
        res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                self.count += len(arr1)
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i += 1
        if i >= len(arr1):
            res += arr2[j:]
        else:
            self.count += len(arr1[i:])
            res += arr1[i:]
        return res

if __name__ == '__main__':
    a = Solution()
    print(a.InversePairs([2,3,4,5,6,7,0,1]))