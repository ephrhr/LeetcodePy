#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        q = deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        while q:
            ans += 1
            temp = deque()
            while q:
                i, j = q.popleft()
                for r, c in [(1,0), (-1, 0), (0, 1), (0, -1)]:
                    ri, cj = r + i, c + j
                    if 0 <= ri < n and 0 <= cj < m and grid[ri][cj] == 0:
                        temp.append((ri, cj))
                        grid[ri][cj] = ans
            q = temp
        return -1 if ans == 1 else ans - 1
# @lc code=end
# DFS
# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         ans = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1: continue
#                 grid[i][j] = 201
#                 if i > 0: grid[i][j] = min(grid[i][j], grid[i - 1][j] + 1)
#                 if j > 0: grid[i][j] = min(grid[i][j], grid[i][j - 1] + 1)
        
#         for i in range(n - 1, -1, -1):
#             for j in range(m - 1, -1, -1):
#                 if grid[i][j] == 1:continue
#                 if i < n - 1: grid[i][j] = min(grid[i][j], grid[i + 1][j] + 1)
#                 if j > m - 1: grid[i][j] = min(grid[i][j], grid[i][j + 1] + 1)
#                 ans = max(ans, grid[i][j])
#         return -1 if ans == 201 else ans - 1

