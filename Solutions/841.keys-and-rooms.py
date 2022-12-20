#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#
from typing import List
from collections import deque
# @lc code=start
# BFS


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = deque([i for i in rooms[0]])
        while q:
            nq = deque()
            while q:
                key = q.popleft()
                if key in visited:
                    continue
                visited.add(key)
                for k in rooms[key]:
                    nq.append(k)
            q = nq
        return len(visited) == len(rooms)

# @lc code=end


# DFS
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set()
#         visited.add(0)

#         def dfs(key):
#             if key in visited:
#                 return
#             visited.add(key)
#             for k in rooms[key]:
#                 if k not in visited:
#                     dfs(k)

#         for k in rooms[0]:
#             dfs(k)
#         return len(visited) == len(rooms)
