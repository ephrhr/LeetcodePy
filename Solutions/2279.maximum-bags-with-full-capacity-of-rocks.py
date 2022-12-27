#
# @lc app=leetcode id=2279 lang=python3
#
# [2279] Maximum Bags With Full Capacity of Rocks
#
from typing import List
# @lc code=start


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        ans = 0
        for i in range(n):
            capacity[i] -= rocks[i]
        if additionalRocks >= sum(capacity):
            return n
        capacity = sorted(capacity)
        for i in range(n):
            if capacity[i] > additionalRocks:
                return ans
            additionalRocks -= capacity[i]
            ans += 1

        return ans
# @lc code=end
