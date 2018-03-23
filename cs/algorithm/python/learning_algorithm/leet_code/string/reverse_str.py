class Solution:
    def ReverseSentence(self, s):
        # write code here
        s = list(s)
        i, j = 0, 0
        while j <= len(s):
            if j == len(s):
                self.reverse(s, i, j - 1)
                j += 1
            elif s[j] != " ":
                j += 1
            else:
                self.reverse(s, i, j - 1)
                i = j + 1
                j += 1
        self.reverse(s, 0, len(s) - 1)
        return "".join(s)

    def reverse(self, s, l, r):

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == '__main__':
    s = "student. a am Ifuck"
    a = Solution()
    print(a.ReverseSentence(s))