import collections
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # filter all positions that equal to 1 in img1 and img2
        img1 = [(i, j) for i, row in enumerate(img1)
                for j, item in enumerate(row) if item]
        img2 = [(i, j) for i, row in enumerate(img2)
                for j, item in enumerate(row) if item]
        # mapping overlap count between every possible translation
        count = collections.Counter((x1-x2, y1-y2)
                                    for x1, y1 in img1 for x2, y2 in img2)
        return max(count.values() or [0])


sol = Solution()
print(sol.largestOverlap([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [
      [0, 0, 0], [0, 1, 1], [0, 0, 1]]))
