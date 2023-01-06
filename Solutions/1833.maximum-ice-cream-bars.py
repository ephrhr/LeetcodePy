#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#
from typing import List
# @lc code=start


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i, cost in enumerate(costs):
            if cost > coins:
                return i
            coins -= cost
        return len(costs)

# @lc code=end
