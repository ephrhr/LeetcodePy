#
# @lc app=leetcode id=1822 lang=python3
#
# [1822] Sign of the Product of an Array
#
from typing import List
# @lc code=start
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for n in nums:
            if n == 0: return 0
            if n < 0: ans *= -1
        return ans
# @lc code=end

