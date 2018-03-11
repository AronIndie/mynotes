def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)

    n = nums[-1]
    n_1 = nums[-2]
    n_2 = nums[-3]

    if n_2 < n_1:
        if n + n_2 >= n_1:
            return rob(nums[:-1]) + n + n_2 - n_1
        else:
            return rob(nums[:-1])

    elif n_2 >= n_1:
        return rob(nums[:1]) + n

if __name__ == '__main__':
    rob([1,2,1,1])