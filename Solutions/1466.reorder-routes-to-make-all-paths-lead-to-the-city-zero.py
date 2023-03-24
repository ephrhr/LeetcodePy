#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#
from typing import List
from collections import defaultdict, deque
# @lc code=start
# BFS
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ans = 0
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        visited = set()
        q = deque([0])
        while q:
            nq = deque()
            while q:
                a = q.popleft()
                visited.add(a)
                for b, cost in graph[a]:
                    if b not in visited:
                        ans += cost
                        nq.append(b)
            q = nq
        
        return ans

# @lc code=end
# DFS
# class Solution:
#     def minReorder(self, n: int, connections: List[List[int]]) -> int:
#         self.ans = 0
#         graph = defaultdict(list)
#         for a, b in connections:
#             graph[a].append((b, 1))
#             graph[b].append((a, 0))
#         visited = set()
        
#         def dfs(a):
#             visited.add(a)
#             for b, cost in graph[a]:
#                 if b not in visited:
#                     self.ans += cost
#                     dfs(b)
#         dfs(0)
#         return self.ans

