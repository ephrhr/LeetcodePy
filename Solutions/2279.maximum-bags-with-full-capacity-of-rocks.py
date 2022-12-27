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
        bags = capacity
        ans = 0
        capableRocks = 0
        for i in range(n):
            bags[i] -= rocks[i]
            capableRocks += bags[i]
        if additionalRocks >= capableRocks:
            return n
        bags = sorted(bags)
        for i in range(n):
            if bags[i] == 0:
                ans += 1
                continue
            if additionalRocks == 0:
                break
            if bags[i] > 0:
                if bags[i] > additionalRocks:
                    return ans
                additionalRocks -= bags[i]
                bags[i] = 0
                ans += 1
        return ans
# @lc code=end
