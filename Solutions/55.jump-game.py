#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
from typing import List
# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if farthest <= i:
                return False
        return farthest >= n - 1
# @lc code=end
