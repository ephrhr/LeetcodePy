#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
from typing import List

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        seen = [False] * n
        color = [False] * n
        self.isNotBiparate = False
        def dfs(node):
            if self.isNotBiparate:
                return
            seen[node] = True
            for next in graph[node]:
                if not seen[next]:
                    color[next] = not color[node]
                    dfs(next)
                else:
                    if color[next] == color[node]:
                        self.isNotBiparate = True
        for i in range(n):
            if not seen[i]:
                dfs(i)
        return not self.isNotBiparate
# @lc code=end

