#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
from typing import List
# @lc code=start
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        module = 10 ** 9 + 7
        memo = [[0] * (n + 1) for _ in range(minProfit + 1)]
        memo[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    memo[min(i + p, minProfit)][j + g] += memo[i][j]
        return sum(memo[minProfit]) % module
# @lc code=end

