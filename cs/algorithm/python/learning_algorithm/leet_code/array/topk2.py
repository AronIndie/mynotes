# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        k = len(numbers) // 2
        num = self.find_topk(numbers, 0, len(numbers) - 1, k)
        count = 0
        for i in numbers:
            if i == num:
                count += 1
        if count <= k:
            return 0
        return num

    def find_topk(self, arr, i, j, k):
        if i >= j:
            return

        l = i
        r = j
        flag = arr[j]
        while i < j:
            while i < j and arr[i] <= flag:
                i += 1
            arr[j] = arr[i]
            while i < j and arr[j] > flag:
                j -= 1
            arr[i] = arr[j]
        arr[i] = flag

        if i == k:
            return arr[i]
        elif i > k:
            return self.find_topk(arr, l, i - 1, k)
        else:
            return self.find_topk(arr, i + 1, r, k)

if __name__ == '__main__':
    a = [1,2,3,2,4,2,5,2,3]
    s = Solution()
    s.MoreThanHalfNum_Solution(a)