#
# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
#
from typing import List
from math import comb
# @lc code=start


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        def dfs(nums):
            n = len(nums)
            if n < 3:
                return 1
            left = [a for a in nums if a < nums[0]]
            right = [a for a in nums if a > nums[0]]
            return dfs(left) * dfs(right) * comb(n - 1, len(left)) % mod

        return (dfs(nums) - 1) % mod
# @lc code=end
