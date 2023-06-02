#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#
from typing import List
from math import sqrt
# @lc code=start


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [set([i]) for i in range(n)]
        ans = 0

        def isOverlap(a, b):
            return (bombs[a][0] - bombs[b][0])**2 + (bombs[a][1] - bombs[b][1])**2 <= bombs[a][2]**2

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isOverlap(i, j):
                    graph[i].add(j)

        def dfs(i, visited):
            for bomb in graph[i]:
                if bomb not in visited:
                    visited.add(bomb)
                    dfs(bomb, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))

        return ans


# @lc code=end
