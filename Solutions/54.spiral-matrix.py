#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
from typing import List
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        left, top, right, bottom = 0, 1, n - 1, m - 1
        # 0: right, 1: down, 2: left, 3: up
        direction = 0
        ans = [matrix[r][c]]        
            
        while len(ans) < m * n:
            # right
            if direction == 0:
                while c < right:
                    c += 1
                    ans.append(matrix[r][c])
                right -= 1
                
            # down
            elif direction == 1:
                while r < bottom:
                    r += 1
                    ans.append(matrix[r][c])
                bottom -= 1
                
            # left
            elif direction == 2:
                while c > left:
                    c -= 1
                    ans.append(matrix[r][c])
                left += 1
                
            # up
            else:
                while r > top:
                    r -= 1
                    ans.append(matrix[r][c])
                top += 1
                
            direction = (direction + 1) % 4
        return ans
# @lc code=end

