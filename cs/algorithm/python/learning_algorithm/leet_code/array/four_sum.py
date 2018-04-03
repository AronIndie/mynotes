class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                pairs.append((i, j, nums[i] + nums[j]))
        pairs = sorted(pairs, key=lambda x: x[2])
        i, j = 0, len(pairs) - 1
        res = []
        while i < j:
            a, b = pairs[i], pairs[j]
            s = a[2] + b[2]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                if a[0] == b[0] or a[0] == b[1] or a[1] == b[0] or a[1] == b[1]:
                    if pairs[i][2] == pairs[i+1][2]:
                        i += 1
                    elif pairs[j][2] == pairs[j-1][2]:
                        j -= 1
                    else:
                        i += 1
                else:
                    combine = [a[0], a[1], b[0], b[1]]
                    combine = [nums[i] for i in combine]
                    combine.sort()
                    res.append(tuple(combine))
                    i += 1
        return list(set(res))


if __name__ == '__main__':
    a = [-3,-1,0,2,4,5]
    b = 2
    s = Solution()
    print(s.fourSum(a, b))
