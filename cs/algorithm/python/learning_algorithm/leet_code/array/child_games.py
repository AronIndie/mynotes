
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        out = []
        ins = list(range(n))
        while len(out) < n - 1:
            pos = m % len(ins) - 1
            out.append(ins.pop(pos))
            if pos != -1:
                ins[:] = ins[pos:] + ins[:pos]

        return ins[0]

    def Sum_Solution(self, n):
        # write code here
        return n and (n + self.Sum_Solution(n - 1))


if __name__ == '__main__':
    s = Solution()
    #print(s.LastRemaining_Solution(6, 7))
    s.Sum_Solution(10)