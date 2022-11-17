#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        areaA = (ax2 - ax1) * (ay2 - ay1)
        areaB = (bx2 - bx1) * (by2 - by1)
        overlapW = min(ax2, bx2) - max(ax1, bx1)
        overlapH = min(ay2, by2) - max(ay1, by1)
        return areaA + areaB - max(overlapH, 0) * max(overlapW, 0)
# @lc code=end

# class Solution:
#     def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
#         if bx1 < ax1:
#             ax1, ax2, ay1, ay2, bx1, bx2, by1, by2 = bx1, bx2, by1, by2, ax1, ax2, ay1, ay2
#         areaA = (ax2 - ax1) * (ay2 - ay1)
#         areaB = (bx2 - bx1) * (by2 - by1)
#         cx1 = cx2 = cy1 = cy2 = 0
#         if ax1 <= bx1 <= ax2 and ay1 <= by2 and by1 <= ay2:
#             cx1 = bx1
#             cx2 = min(ax2, bx2)
#             cy1 = max(ay1, by1)
#             cy2 = min(ay2, by2)

#         overlap = (cx2 - cx1) * (cy2 - cy1)
#         return areaA + areaB - overlap
