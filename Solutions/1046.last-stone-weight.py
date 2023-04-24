#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [s * -1 for s in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            if first != second:
                heapq.heappush(pq, first - second)
        return pq[0] * -1 if pq else 0
            
            
# @lc code=end

