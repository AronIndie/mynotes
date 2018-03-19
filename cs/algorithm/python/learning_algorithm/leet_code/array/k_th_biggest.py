# -*- coding:utf-8 -*-

"""
寻找第k大的数，算法复杂度O(1)
"""

def find_kth_biggest(nums, k):

    if not nums:
        return -1


    target = nums[-1]
    i = 0
    j = len(nums) - 1

    while i < j:
        while nums[i] < target and i < j:
            i += 1

        nums[j] = nums[i]
        while nums[j] > target and i < j:
            j -= 1

        nums[i] = nums[j]

    nums[i] = target

    if i == k:
        return nums[i]

    left = nums[:i]
    right = nums[i+1:]

    if i > k:
        return find_kth_biggest(left, k)
    else:
        return find_kth_biggest(right, k-len(left)-1)


if __name__ == '__main__':
    a = [-2,10,3,0,-1,6,7,8,1,2,4,11,20]
    print(find_kth_biggest(a, 3))