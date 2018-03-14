

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = 0
        while j < len(numbers) and i < len(numbers):
            if i == j:
                j += 1
                continue

            if numbers[i] + numbers[j] == target:
                return [i, j]

            elif numbers[i] + numbers[j] < target:
                if j < len(numbers)-1:
                    j += 1
                else:
                    i += 1
            else:
                j -= 1
                i += 1

        return [i, j]

if __name__ == '__main__':
    nums = [5, 25, 75]
    a = Solution()
    print(a.twoSum(nums, 100))