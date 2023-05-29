#
# @lc app=leetcode id=1140 lang=python3
#
# [1140] Stone Game II
#
from typing import List
# @lc code=start
# Since the number of stones in the piles is constant,
# the more stones Alice gets, the less Bob does, and vice versa.


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[-1] * (n + 1) for i in range(n + 1)] for player in range(0, 2)]
        # player: 0: Alice, 1: Bob

        # play(player, i, m) will return the maximum stones
        # player can recieves and all players play optimally.
        def play(player, i, m):
            if i == n:
                return 0
            if dp[player][i][m] != -1:
                return dp[player][i][m]
            ans = -1 if player == 0 else 10000000
            # stones recieves in current move.
            stones = 0
            for x in range(1, min(2 * m, n - i) + 1):
                stones += piles[i + x - 1]
                if player == 0:
                    # Alice will get stones after her current move.
                    # she will choose the value x that maximizes this value.
                    ans = max(ans, stones + play(1, i + x, max(m, x)))
                else:
                    # Bob wants to minimize the number of stones Alice receives,
                    # and thus Bob wants to minimize the return value of play().
                    ans = min(ans, play(0, i + x, max(m, x)))
            dp[player][i][m] = ans
            return ans

        return play(0, 0, 1)
# @lc code=end
