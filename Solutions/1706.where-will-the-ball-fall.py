#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#
from typing import List
# @lc code=start


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        memo = [[0] * n for _ in range(m)]

        def dp(r: int, c: int) -> int:
            if r >= m:
                return c
            if memo[r][c] != 0:
                return memo[r][c]
            nextC = -1
            if grid[r][c] == 1 and c + 1 < n and grid[r][c + 1] == 1:
                nextC = dp(r + 1, c + 1)
            if grid[r][c] == -1 and c - 1 >= 0 and grid[r][c - 1] == -1:
                nextC = dp(r + 1, c - 1)
            memo[r][c] = nextC
            return nextC
        return [dp(0, i) for i in range(n)]

# @lc code=end

# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         m, n = len(grid), len(grid[0])

#         def check(c):
#             for r in range(m):
#                 nextC = c + grid[r][c]
#                 if nextC < 0 or nextC >= n or grid[r][nextC] != grid[r][c]:
#                     return -1
#                 c = nextC
#             return c
#         return map(check, range(n))


# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         m = len(grid)
#         n = len(grid[0])
#         dp = [[i for i in range(n)] for _ in range(m + 1)]
#         for r in range(m - 1, -1, -1):
#             for c in range(n):
#                 nextC = c + grid[r][c]
#                 if nextC < 0 or nextC == n or grid[r][nextC] != grid[r][c]:
#                     dp[r][c] = -1
#                 else:
#                     dp[r][c] = dp[r + 1][nextC]
#         return dp[0]
