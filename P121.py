from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for n in prices:
            lowest = min(lowest, n)
            profit = max(profit, n - lowest)
        return profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
