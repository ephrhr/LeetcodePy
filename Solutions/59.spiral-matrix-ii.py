#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
from typing import List
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[1 for c in range(n)] for r in range(n)]
        direction = 0
        left, right, top, bottom = 0, n - 1, 1, n - 1
        r, c = 0, 0
        count = 2
        while count <= n * n:
            # right
            if direction == 0:
                while c < right:
                    c += 1
                    ans[r][c] = count
                    count += 1
                right -= 1
            # down
            elif direction == 1:
                while r < bottom:
                    r += 1
                    ans[r][c] = count
                    count += 1
                bottom -= 1
            # left
            elif direction == 2:
                while c > left:
                    c -= 1
                    ans[r][c] = count
                    count += 1
                left += 1
            # up
            else:
                while r > top:
                    r -= 1
                    ans[r][c] = count
                    count += 1
                top += 1
                
            direction = (direction + 1) % 4
        return ans
# @lc code=end

