#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#
from typing import List
import bisect
# @lc code=start


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[-1][-1] >= 0:
            return 0
        if grid[0][0] < 0:
            return m * n
        ans = 0
        index = 0
        for r in reversed(range(m)):
            row = grid[r]
            index = bisect.bisect_right(
                row, 0, lo=index, key=lambda x: -x)
            if index == n:
                return ans
            ans += n - index
        return ans
# @lc code=end

# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         ans = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] < 0:
#                     ans += n - j
#                     break
#         return ans
