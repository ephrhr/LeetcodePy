#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#
from typing import List
# @lc code=start


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        def calculateSlope(a, b):
            x0, y0 = a
            x1, y1 = b
            if x1 - x0 == 0:
                return float('inf')
            return (y1 - y0) / (x1 - x0)

        slope = calculateSlope(coordinates[0], coordinates[1])

        for node in coordinates[2:]:
            if calculateSlope(coordinates[0], node) != slope:
                return False

        return True

# @lc code=end
