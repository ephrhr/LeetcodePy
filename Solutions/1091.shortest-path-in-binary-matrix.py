#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
from typing import List
from collections import deque
# @lc code=start


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        directions = [[-1, -1], [-1, 0], [-1, 1],
                      [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        visited = [[False for _ in range(n)] for _ in range(n)]
        q = deque()
        q.appendleft([n-1, n-1])
        while q:
            nq = deque()
            ans += 1
            while q:
                i, j = q.pop()
                if visited[i][j] or grid[i][j] == 1:
                    continue
                visited[i][j] = True
                if i == 0 and j == 0:
                    return ans
                for x, y in directions:
                    if 0 <= i + x < n and 0 <= j + y < n and not visited[i + x][j + y]:
                        nq.appendleft([i + x, j + y])
            q = nq
        return ans if visited[0][0] else -1
# @lc code=end
