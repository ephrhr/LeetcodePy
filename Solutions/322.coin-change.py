#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
from typing import List
# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [(amount + 1) for _ in range(amount + 1)]

        memo[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                memo[i] = min(memo[i], memo[i - coin] + 1)
        return memo[amount] if memo[amount] != amount + 1 else -1
# @lc code=end
# recursion solution
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         memo = [None for _ in range(amount + 1)]

#         def dp(amount):
#             if amount == 0:
#                 return 0
#             if amount < 0:
#                 return -1
#             if memo[amount]:
#                 return memo[amount]
#             ans = float('inf')
#             for coin in coins:
#                 sub = dp(amount - coin)
#                 if sub == -1:
#                     continue
#                 ans = min(ans, sub + 1)
#             memo[amount] = -1 if ans == float('inf') else ans
#             return memo[amount]
#         return dp(amount)
