#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
from typing import List
# @lc code=start

# memo[i][k][0 or 1]
# 0 <= i <= n - 1, 1 <= k <= K
# n 为天数，大 K 为交易数的上限，0 和 1 代表是否持有股票。


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = [[None, None] for _ in range(n)]

        for i in range(n):
            if i - 1 == -1:
                memo[i][0] = 0
                memo[i][1] = -prices[i]
                continue
            if i - 2 == -1:
                memo[i][0] = max(memo[i - 1][0], memo[i - 1][1] + prices[i])
                memo[i][1] = max(memo[i - 1][1], -prices[i])
                continue
            memo[i][0] = max(memo[i - 1][0], memo[i - 1][1] + prices[i])
            memo[i][1] = max(memo[i - 1][1], memo[i - 2][0] - prices[i])

        return memo[n - 1][0]

# @lc code=end
