#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#
from typing import List
from collections import deque
# @lc code=start


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) - 1
        ans = []

        def dfs(path: List[int]):
            if path[-1] == n:
                ans.append(path)
            else:
                for next in graph[path[-1]]:
                    dfs(path + [next])

        dfs([0])
        return ans

# @lc code=end

# BFS
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         n = len(graph) - 1
#         ans = []
#         q = deque([[0]])
#         while q:
#             path = q.popleft()
#             if path[-1] == n:
#                 ans.append(path)
#             else:
#                 q.extend(path + [next] for next in graph[path[-1]])
#         return ans
