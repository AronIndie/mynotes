class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here

        if index == 1:
            return 1

        factors = [2, 3, 5]
        cand = []
        res = [1]
        count = 1
        while count < index:
            if not cand:
                num = factors.pop(0)
            elif not factors:
                num = cand.pop(0)
            else:
                if factors[0] < cand[0]:
                    num = factors.pop(0)
                else:
                    num = cand.pop(0)
            if num == res[-1]: continue
            res.append(num)
            for i in range(1, len(res)):
                self.insert(cand, res[i] * num)
            count += 1
        return res[-1]

    def insert(self, arr, i):
        for j, num in enumerate(arr):
            if num > i:
                arr.insert(j, i)
                break
        else:
            arr.append(i)


if __name__ == '__main__':
    s = Solution()
    print(s.GetUglyNumber_Solution(1000))