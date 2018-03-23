class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        _max = [0, ""]
        arr = [[False for j in range(i+1)] for i in range(len(s))]
        for i in range(len(arr)):
            for j in range(i + 1):
                if i == j:
                    arr[i][j] = True
                elif arr[i] == arr[j]:
                    if i - j == 1:
                        arr[i][j] = True
                    else:
                        arr[i][j] = a[i-1][j+1]

                if arr[i][j]:
                    if i - j > _max[0]:
                        _max = [i-j, s[j:i+1]]
        return _max[1]


    dic = {}

    def longestPalindrome2(self, arr):
        if arr in self.dic:
            res = self.dic[arr]
        else:
            res = self.isPalindrome(arr)

        if res:
            return arr
        else:
            l = self.longestPalindrome2(arr[1:])
            r = self.longestPalindrome2(arr[:-1])
            return l if len(l) > len(r) else r

    def isPalindrome(self, arr):
        res = False
        if not arr:
           pass
        elif len(arr) == 1:
            res = True
        elif len(arr) == 2:
            if arr[0] == arr[1]:
                res =  True

        elif arr[0] == arr[-1]:
            res = self.isPalindrome(arr[1:-1])
        self.dic[arr] = res
        return res


if __name__ == '__main__':
    a = "dasdfdhfdfakkafdfhdasef"
    s = Solution()
    # print(s.longestPalindrome(a))
    print(s.longestPalindrome2(a))