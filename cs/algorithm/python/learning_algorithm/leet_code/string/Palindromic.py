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

if __name__ == '__main__':
    a = "babad"
    s = Solution()
    print(s.longestPalindrome(a))