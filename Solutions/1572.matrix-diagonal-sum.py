#
# @lc app=leetcode id=1572 lang=python3
#
# [1572] Matrix Diagonal Sum
#
from typing import List
# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = sum(mat[i][i] + mat[n - 1 - i][i] for i in range(n))
        return ans if n % 2 == 0 else ans - mat[n // 2][n // 2]
# @lc code=end

