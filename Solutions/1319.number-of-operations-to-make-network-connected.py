#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#
from typing import List
# @lc code=start
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) + 1 < n: 
            return -1
        
        graph = [set() for _ in range(n)]
        
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
        visited = [False] * n
        
        def dfs(a):
            if visited[a]: return 0
            visited[a] = True
            for b in graph[a]:
                dfs(b)
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1
# @lc code=end

