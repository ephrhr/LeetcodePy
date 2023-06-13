#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#
from typing import List
# @lc code=start


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        transGrid = [[grid[c][r] for c in range(n)] for r in range(n)]
        for i in range(n):
            for j in range(n):
                ans += grid[i] == transGrid[j]

        return ans
# @lc code=end
