#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
from typing import List
from collections import deque
# @lc code=start
# DFS
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirctions = [1, 0, -1, 0, 1]
        ans = 0
        
        def dfs(r, c):
            if r in (0, m - 1) or c in (0, n - 1):
                self.isIsland = False 
            for i in range(4):
                nr = r + dirctions[i]
                nc = c + dirctions[i + 1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = -1 
                    dfs(nr, nc)
                    
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    self.isIsland = True
                    dfs(r, c)
                    ans += self.isIsland
                    
        return ans 
# @lc code=end
# BFS
# class Solution:
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         visited = [[False for c in range(n)] for r in range(m)]
#         dirctions = [1, 0, -1, 0, 1]
#         ans = 0
#         q = deque()
        
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == 0:
#                     q.append([r, c])
                    
#         while q:
#             nq = deque([q.popleft()])
#             closed = True
#             hasLand = False
#             while nq:
#                 (r, c) = nq.popleft()
#                 if visited[r][c]: continue
#                 visited[r][c] = True
#                 hasLand = True
#                 for i in range(4):
#                     nr = r + dirctions[i]
#                     nc = c + dirctions[i + 1]
#                     if nr >= m or nr < 0 or nc >= n or nc < 0:
#                         closed = False
#                     elif grid[nr][nc] == 0:
#                         nq.append([nr, nc])
#             if closed and hasLand:
#                 ans += 1
                
#         return ans
