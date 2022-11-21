#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#
from typing import List
from collections import deque
# @lc code=start


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        def reached(p, q): return (not p == entrance[0] or not q == entrance[1]) and (
            p == 0 or q == 0 or p == m - 1 or q == n - 1)

        q, ans = deque(), 0
        q.append((entrance[0], entrance[1], ans))
        directions = [1, 0, -1, 0, 1]
        while q:
            row, col, ans = q.popleft()
            for i in range(4):
                r, c = row + directions[i], col + directions[i + 1]
                if r < 0 or c < 0 or r == m or c == n or maze[r][c] == '+':
                    continue
                if reached(r, c):
                    return ans + 1
                maze[r][c] = '+'
                q.append((r, c, ans + 1))
        return -1
# @lc code=end
