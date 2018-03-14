class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1], nums[0] + nums[1])

        mid = len(nums) // 2
        left = nums[: mid]
        right = nums[mid:]

        left_max, right_max = left[-1], right[0]
        temp1, temp2 = left_max, right_max

        for i in range(len(left)-1, 0, -1):
            temp1 += left[i]
            if temp1 > left_max:
                left_max = temp1

        for i in range(1, len(right)):
            temp2 += right[i]
            if temp2 > right_max:
                right_max = temp2

        return max(self.maxSubArray(left), self.maxSubArray(right), left_max + right_max)


if __name__ == '__main__':
    a = Solution()
    a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])