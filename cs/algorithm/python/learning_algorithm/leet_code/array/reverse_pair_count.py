# -*- coding:utf-8 -*-

class Solution:
    def InversePairs(self, data):
        self.merge_sort(data)
        return self.count

    def merge_sort(self, arr):
        if not arr:
            return []

        if len(arr) == 1:
            return arr

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    count = 0
    def merge(self, arr1, arr2):
        res = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):

            if arr1[i] > arr2[j]:
                res.append(arr2[j])
                j += 1
            else:
                res.append(arr1[i])
                i+= 1
                self.count += j

        if i < len(arr1):
            res += arr1[i:]
            self.count += j * len(arr1[i:])
        else:
            res += arr2[j:]

        return res

if __name__ == '__main__':
    a = [1,2,3,4]
    b = [0,5,6,7]
    s = Solution()
    print(s.InversePairs([1,2,3,4,5,6,7,0]))
    print(s.count)
