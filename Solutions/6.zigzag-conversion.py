#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        step = (numRows == 1) - 1
        rows, i = [''] * numRows, 0
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows - 1:
                step *= -1  # reversed direction
            i += step
        return ''.join(rows)
# @lc code=end
