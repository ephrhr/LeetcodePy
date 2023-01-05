#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#
from typing import List
# @lc code=start


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda x: x[1])
        arrowPos = float('-inf')
        for i in range(len(points)):
            s, e = points[i][0], points[i][1]
            if arrowPos < s:
                ans += 1
                arrowPos = e
        return ans
# @lc code=end
