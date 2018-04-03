class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return None
        s = 999
        for i, num in enumerate(nums):
            if i > len(nums) - 3:
                break
            new_t = target - num
            _min = self.twoSumClosest(nums[i + 1:], new_t)
            if abs(_min[0] + _min[1] + num - target) < abs(s - target):
                s = _min[0] + _min[1] + num
        return s

    def twoSumClosest(self, nums, target):
        if len(nums) == 2:
            return (nums[0], nums[1], 0)
        _min = (0, 0, 999)
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if abs(s - target) < abs(_min[2]):
                _min = (nums[i], nums[j], abs(s - target))
            if s < target:
                i += 1
            elif s > target:
                j -= 1
            else:
                return (nums[i], nums[j], 0)


        return _min

if __name__ == '__main__':
    a = [-1,2,1,-4]
    t = 1
    s = Solution()
    print(s.threeSumClosest(a, t))