#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
from typing import List
# @lc code=start


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = [[None for r in range(n)]
                for c in range(n)]

        def dp(i: int, j: int):
            if j < 0 or j >= n:
                return None
            if i == n - 1:
                memo[i][j] = matrix[i][j]
                return memo[i][j]
            if memo[i][j] is not None:
                return memo[i][j]
            next = []
            left = dp(i + 1, j - 1)
            mid = dp(i + 1, j)
            right = dp(i + 1, j + 1)
            if left is not None:
                next.append(left)
            if mid is not None:
                next.append(mid)
            if right is not None:
                next.append(right)
            memo[i][j] = matrix[i][j] + min(next)
            return memo[i][j]

        ans = []
        for j in range(n):
            ans.append(dp(0, j))
        return min(ans)
# @lc code=end
