#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
from typing import List
# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empties, placedflowers = 1, 0
        for f in flowerbed:
            if f == 0:
                empties += 1
            else:
                placedflowers += (empties - 1) // 2
                empties = 0
                if placedflowers >= n: return True
        return placedflowers + empties // 2 >= n
# @lc code=end

