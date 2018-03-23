class Solution:
    def reOrderArray(self, array):
        # write code here
        i, j = 0, 0
        while i < len(array) and j < len(array):
            if array[j] % 2 == 1 and j > i:
                self.insert(array, i, j)
                i, j = j, i

            if array[i] % 2 == 1:
                i += 1
            else:
                j += 1

        return array

    def insert(self, arr, l, r):
        temp = arr[r]
        for i in range(r, l, -1):
            arr[i] = arr[i - 1]
        arr[l] = temp


# -*- coding:utf-8 -*-
class Solution2:
    def reOrderArray(self, array):
        # write code here
        i, j = 0, 0
        while i < len(array) and j < len(array):
            if array[i] % 2 == 0:
                j = i
                while array[j] % 2 == 0:
                    j += 1
                    if j == len(array):
                        return array
                self.insert(array, i, j)
                i, j = j, i
            else:
                i += 1
        return array

    def insert(self, arr, i, j):
        temp = arr[j]
        for k in range(j, i, -1):
            arr[k] = arr[k - 1]
        arr[i] = temp


if __name__ == '__main__':
    a = [1,3,5,7,2,4,6]
    s = Solution2()
    print(s.reOrderArray(a))