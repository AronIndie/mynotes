# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput:
            return None
        if k == 0:
            return []
        i = self.find_topk(tinput, k, 0, len(tinput) - 1)
        return [i]

    def find_topk(self, arr, k, i, j):
        if i >= j:
            return

        l, r = i, j
        flag = arr[j]
        while i < j:
            while i < j and arr[i] < flag:
                i += 1
            arr[j] = arr[i]
            while i < j and arr[j] > flag:
                j -= 1
            arr[i] = arr[j]
        arr[i] = flag

        if i == k:
            return i
        elif i > k:
            return self.find_topk(arr, k, l, i - 1)
        else:
            return self.find_topk(arr, k, i + 1, r)

if __name__ == '__main__':
    s = Solution()
    s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4)