#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from typing import List
# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        top = [None for _ in range(len(nums))]
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]
            left, right = 0, piles
            while left < right:
                mid = (left + right) // 2
                if top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid
            if left == piles:
                piles += 1
            top[left] = poker
        return piles
# @lc code=end
# TC: O(n^2) DP Solution
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         memo = [1 for _ in range(len(nums))]
#         for i in range(len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     memo[i] = max(memo[i], memo[j] + 1)
#         ans = 0
#         for i in range(len(memo)):
#             ans = max(ans, memo[i])
#         return ans
