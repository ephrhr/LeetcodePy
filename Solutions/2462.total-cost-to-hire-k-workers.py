#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#
from typing import List
import heapq
# @lc code=start


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        hired = 0
        ans = 0
        if len(costs) <= candidates * 2:
            heapq.heapify(costs)
            while hired < k:
                ans += heapq.heappop(costs)
                hired += 1
        else:
            headSkipped = candidates
            heads = costs[:candidates]
            tailSkipped = len(costs) - candidates - 1
            tails = costs[-candidates:]
            heapq.heapify(heads)
            heapq.heapify(tails)
            while hired < k:
                if not tails or heads and heads[0] <= tails[0]:
                    ans += heapq.heappop(heads)
                    if headSkipped <= tailSkipped:
                        heapq.heappush(heads, costs[headSkipped])
                        headSkipped += 1
                else:
                    ans += heapq.heappop(tails)
                    if headSkipped <= tailSkipped:
                        heapq.heappush(tails, costs[tailSkipped])
                        tailSkipped -= 1
                hired += 1
        return ans
# @lc code=end
