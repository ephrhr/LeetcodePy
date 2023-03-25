#
# @lc app=leetcode id=2316 lang=python3
#
# [2316] Count Unreachable Pairs of Nodes in an Undirected Graph
#
from typing import List
# @lc code=start
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ans = n * (n - 1) // 2
        graph = [set([i]) for i in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
            
        visited = set()
        def dfs(a):
            visited.add(a)
            self.count += 1
            for b in graph[a]:
                if b not in visited:
                    dfs(b)
        
        for a in range(n):
            if a not in visited:
                self.count = 0
                dfs(a)
                ans -= (self.count * (self.count - 1)) // 2

        return ans
# @lc code=end

