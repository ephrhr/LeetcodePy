#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [{} for _ in range(n + 1)]
        for a, b, d in roads:
            graph[a][b] = graph[b][a] = d
            
        visited = set()
        minScore = 10**4
        q = deque([1])
        
        while q:
            nq = deque()
            while q:
                city = q.popleft()
                for (nextCity, distance) in graph[city].items():
                    if nextCity not in visited:
                        nq.append(nextCity)
                        visited.add(nextCity)
                    minScore = min(minScore, distance)
            q = nq
            
        return minScore
# @lc code=end

