#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        left, right = 0, nums[0]
        ans = 1
        while right < n - 1:
            ans += 1
            next = max(i + nums[i] for i in range(left, right + 1))
            left, right = right, next
        return ans
# @lc code=end
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2: return 0
#         dp = [0] * n
#         j = 0
#         for i in range(1, n):
#             while j + nums[j] < i:
#                 j += 1
#             dp[i] = dp[j] + 1
#         return dp[-1]

