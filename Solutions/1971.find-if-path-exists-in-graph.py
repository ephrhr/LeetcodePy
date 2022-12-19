#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#
from collections import defaultdict
from typing import List
# @lc code=start
# BFS


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        q = [source]
        seen = set([source])
        while q:
            nq = []
            for node in q:
                if node == destination:
                    return True
                for n in neighbors[node]:
                    if n not in seen:
                        seen.add(n)
                        nq.append(n)
            q = nq
        return False
# @lc code=end

# DFS
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         neighbors = defaultdict(list)
#         for u, v in edges:
#             neighbors[u].append(v)
#             neighbors[v].append(u)

#         def dfs(node: int, seen: set):
#             if node == destination:
#                 return True
#             if node in seen:
#                 return False

#             seen.add(node)
#             for n in neighbors[node]:
#                 if dfs(n, seen):
#                     return True
#             return False

#         return dfs(source, set())
