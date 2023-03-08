#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
from typing import List
# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        def neededHours(speed):
            return sum((p - 1) // speed + 1 for p in piles)
        while left < right:
            mid = (left + right) // 2
            if neededHours(mid) > h:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

