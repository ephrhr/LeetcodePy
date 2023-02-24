#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq = []
        projects = sorted(zip(profits, capital), key=lambda l: l[1])
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][1] <= w:
                heapq.heappush(pq, -projects[i][0])
                i += 1
            if pq:
                w -= heapq.heappop(pq)
        return w
# @lc code=end

