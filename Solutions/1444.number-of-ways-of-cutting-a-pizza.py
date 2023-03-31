#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#
from typing import List
from functools import lru_cache
# @lc code=start
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n, mod = len(pizza), len(pizza[0]), 10 ** 9 + 7
        apples = [[0] * (n + 1) for r in range(m + 1)] 
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                apples[r][c] = (pizza[r][c] == 'A') + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]
        @lru_cache(None)
        def dp(remain, r, c):
            if apples[r][c] == 0: return 0
            if remain == 0: return 1
            val = 0
            for nr in range(r + 1, m):
                if apples[r][c] - apples[nr][c] > 0:
                    val += dp(remain - 1, nr, c)
            for nc in range(c + 1, n):
                if apples[r][c] - apples[r][nc] > 0:
                    val += dp(remain - 1, r, nc)
            return val % mod

        return dp(k - 1, 0, 0)
# @lc code=end

