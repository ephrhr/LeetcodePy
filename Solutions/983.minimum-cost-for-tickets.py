#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
from typing import List
# @lc code=start
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daySet = set(days)
        memo = [0 for _ in range(days[-1] + 1)]
        
        for i in range(1, days[-1] + 1):
            if i not in daySet:
                memo[i] = memo[i - 1]
                continue
            memo[i] = min(memo[i - 1] + costs[0], min(memo[max(i - 7, 0)] + costs[1], memo[max(i - 30, 0)] + costs[2]))
        
        return memo[-1]
# @lc code=end

