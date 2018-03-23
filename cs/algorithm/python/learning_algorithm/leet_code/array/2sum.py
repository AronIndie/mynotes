class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return None
        i = 0
        j = len(array) - 1
        _max = []
        while i < j:
            s = array[i] + array[j]
            if s < tsum:
                i += 1
            elif s > tsum:
                j -= 1
            else:
                t = array[i] * array[j]
                if not _max:
                    _max = [array[i], array[j], t]
                else:
                    if t < _max[2]:
                        _max = [array[i], array[j], t]
                j -= 1
        print(_max[0])
        print(_max[1])

if __name__ == '__main__':
    a = [1,2,4,7,11,15]
    b = 15
    s = Solution()
    s.FindNumbersWithSum(a, b)