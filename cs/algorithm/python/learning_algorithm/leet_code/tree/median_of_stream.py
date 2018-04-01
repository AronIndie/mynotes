# -*- coding:utf-8 -*-
class Solution:
    heap1 = []  # 大顶堆
    heap2 = []  # 小顶堆
    length = 0
    def Insert(self, num):
        if not self.heap1:
            self.heap1.append(num)
            self.length += 1
            return

        if self.length % 2 == 0: # 长度为偶数时，插入大顶堆
            if num < self.heap2[0]:
                self.heap1.insert(0, num)
                self.adj_big_heap(self.heap1, 0)
            else:
                self.heap1.insert(0, self.heap2.pop(0))
                self.heap2.insert(0, num)
                self.adj_big_heap(self.heap1, 0)
                self.adj_small_heap(self.heap2, 0)
        else:
            if num < self.heap1[0]:
                self.heap2.insert(0, self.heap1.pop(0))
                self.heap1.insert(0, num)
                self.adj_big_heap(self.heap1, 0)
                self.adj_small_heap(self.heap2, 0)
            else:
                self.heap2.insert(0, num)
                self.adj_small_heap(self.heap2, 0)
        self.length += 1


    def adj_two_heap(self):
        l1 = len(self.heap1)
        l2 = len(self.heap2)
        if l1 == l2 or l1 - l2 == 1:
            return
        if l2 > l1:
            while len(self.heap2) > len(self.heap1):
                self.heap1.insert(0, self.heap2.pop(0))
                self.adj_big_heap(self.heap1, 0)
                self.adj_small_heap(self.heap2, 0)
        else:
            while len(self.heap1) - len(self.heap2) > 1:
                self.heap2.insert(0, self.heap1.pop(0))
                self.adj_big_heap(self.heap1, 0)
                self.adj_small_heap(self.heap2, 0)

    def adj_big_heap(self, arr, i):
        temp = arr[i]
        k = 2 * i + 1
        while k < len(arr):
            if k + 1 < len(arr) and arr[k + 1] > arr[k]:
                k += 1
            if temp < arr[k]:
                arr[i] = arr[k]
                i = k
            else:
                break
            k = 2 * k + 1
        arr[i] = temp

    def adj_small_heap(self, arr, i):
        temp = arr[i]
        k = 2 * i + 1
        while k < len(arr):
            if k + 1 < len(arr) and arr[k + 1] < arr[k]:
                k += 1
            if temp > arr[k]:
                arr[i] = arr[k]
                i = k
            else:
                break
            k = 2 * k + 1
        arr[i] = temp

    def GetMedian(self):
        # write code here
        if not self.heap1:
            return None

        if not self.heap2:
            return self.heap1[0]

        if len(self.heap1) == len(self.heap2):
            return (self.heap1[0] + self.heap2[0]) / 2
        else:
            return self.heap1[0]

if __name__ == '__main__':
    s = Solution()
    for i in [5,2,3,4,1,6,7,0,8]:
        s.Insert(i)
        print(s.GetMedian())