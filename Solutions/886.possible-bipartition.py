#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
from typing import List
from collections import defaultdict
# @lc code=start

# BFS


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        group_mapping = {}
        for (a, b) in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        for i in range(1, n + 1):
            if i in visited:
                continue
            stack = [(i, 0)]
            while stack:
                nStack = []
                while stack:
                    curr, group = stack.pop()
                    if curr in group_mapping and group != group_mapping[curr]:
                        return False
                    if curr in visited:
                        continue
                    group_mapping[curr] = group
                    visited.add(curr)
                    for child in graph[curr]:
                        nStack.append((child, not group))
                stack = nStack
        return True

# @lc code=end

# UF
# class UF:
#     def __init__(self, n):
#         self.p = [i for i in range(n+1)]

#     def find(self, i):                                        # Find parent
#         if i != self.p[i]:
#             self.p[i] = self.find(self.p[i])
#         return self.p[i]

#     def union(self, j, parent_dislike_i, parent_i):
#         p_j = self.find(j)
#         self.p[p_j] = parent_dislike_i
#         return p_j != parent_i                                # Check if there is a parent conflict

# class Solution:
#     def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
#         self.graph = defaultdict(list)            # Create graph and initilize union find
#         uf = UF(N)
#         for (u, v) in dislikes:
#             self.graph[u].append(v)
#             self.graph[v].append(u)

#         for i in range(1, N+1):
#             parent_i = uf.find(i)
#             if parent_i in self.graph:
#                 parent_dislike_i = uf.find(self.graph[i][0])  # Pick a dislike node's parent as a common parent for the rest of dislike nodes
#                 for dis in self.graph[i][1:]:                 # For each dislike node
#                     if not uf.union(dis, parent_dislike_i, parent_i): return False   # Return False if there is a conflict when grouping
#         return True

# DFS
# class Solution:
#     def dfs(self, i, group):
#         if i in self.group_mapping and group != self.group_mapping[i]:   # Check if there is a conflict
#             return False                                                 # between given group and existing group
#         self.group_mapping[i] = group
#         if i not in self.visited:
#             self.visited.add(i)
#             for dis in self.graph[i]:                                    # DFS for each dislike node recursively
#                 if not self.dfs(dis, not group): return False            # Assign contrary group to dislike node
#         return True

#     def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
#         self.graph = defaultdict(list)
#         self.visited, self.group_mapping = set(), {}
#         for (u, v) in dislikes:                                          # Create graph
#             self.graph[u].append(v)
#             self.graph[v].append(u)

#         for i in range(1, N+1):                                          # DFS until eror
#             if i not in self.visited:                                    # We don't want to revisit since it's DFS
#                 if not self.dfs(i, True):                                # If conflict occurs during DFS, return False
#                     return False
#         return True
