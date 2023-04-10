#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
from typing import List
# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirctions = [1, 0, -1, 0, 1]
        ans = 0
        
        def dfs(r, c):
            if r < 0 or c < 0 or r > m - 1 or c > n - 1 or grid[r][c] != 1: return
            grid[r][c] = -1
            for i in range(4):
                nr = r + dirctions[i]
                nc = c + dirctions[i + 1]
                dfs(nr, nc)
                
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                    dfs(r, c)
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    ans += 1
        
        return ans
# @lc code=end

