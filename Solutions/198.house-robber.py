#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List
# @lc code=start


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(prev + num, curr)
        return curr
# @lc code=end

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         memo = [-1 for _ in range(n)]

#         def dp(i):
#             if i >= n:
#                 return 0
#             if i + 2 >= n:
#                 memo[i] = nums[i]
#             if memo[i] > -1:
#                 return memo[i]
#             next = [dp(j) for j in range(i + 2, n)]
#             memo[i] = nums[i] + max(next)
#             return memo[i]

#         ans = []
#         for i in range(n):
#             ans.append(dp(i))
#         return max(ans)
