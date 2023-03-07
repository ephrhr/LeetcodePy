#
# @lc app=leetcode id=2187 lang=python3
#
# [2187] Minimum Time to Complete Trips
#
from typing import List
# @lc code=start
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, min(time) * totalTrips
        def calculateTrips(targetTime):
            return sum(targetTime // t for t in time)
        while left < right:
            mid = (left + right) // 2
            if calculateTrips(mid) < totalTrips:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

