# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        return self.search(0, 0, rows, cols, threshold)
    reached = set()
    def search(self, x, y, r, c, k):
        _sum = eval("+".join(str(x) + str(y)))
        if _sum > k:
            return 0
        self.reached.add((x, y))
        left, right, down, up = 0, 0, 0, 0
        if x - 1 >= 0 and (x - 1, y) not in self.reached:
            left = self.search(x - 1, y, r, c, k)
        if x + 1 < r and (x + 1, y) not in self.reached:
            right = self.search(x + 1, y, r, c, k)
        if y - 1 >= 0 and (x, y - 1) not in self.reached:
            down = self.search(x, y - 1, r, c, k)
        if y + 1 < c and (x, y + 1) not in self.reached:
            up = self.search(x, y + 1, r, c, k)
        return sum([left, right, down, up]) + 1

if __name__ == '__main__':
    s = Solution()
    print(s.movingCount(15,20,20))