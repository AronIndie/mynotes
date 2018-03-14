class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        if len(cost) == 0:
            return 0

        elif len(cost) <= 2:
            return min(cost)

        n_1, n_2 = 0, 0
        for i in range(2, len(cost)):
            n_ = min(n_1 + cost[i - 1], n_2 + cost[i - 2])
            n_2 = n_1
            n_1 = n_

        return min(n_1 + cost[-1], n_2 + cost[-2])

if __name__ == '__main__':
    a = Solution()
    print(a.minCostClimbingStairs([1, 0, 1, 0]))