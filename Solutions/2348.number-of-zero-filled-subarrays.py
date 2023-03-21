#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = zeroIndex = 0
        for num in nums:
            if num == 0:
                zeroIndex += 1
                ans += zeroIndex
            else:
                zeroIndex = 0
        return ans
                
# @lc code=end
# class Solution:
#     def zeroFilledSubarray(self, nums: List[int]) -> int:
#         ans = 0
#         counter = defaultdict(int)
#         l = r = 0
#         for i in range(len(nums)):
#             if i == len(nums) - 1 and nums[i] == 0:
#                 if nums[i - 1] != 0:
#                     l = i
#                 r = i + 1
#                 counter[r - l] += 1
#             elif nums[i] == 0 and (i == 0 or nums[i - 1] != 0):
#                 l = i
#             elif i > 0 and nums[i] != 0 and nums[i - 1] == 0:
#                 r = i
#                 counter[r - l] += 1
#         if len(counter) == 0:
#             return ans
#         for i in range(max(counter.keys()),0,-1):
#             if i not in counter: continue
#             n = counter[i]
#             ans += n * (i + 1) * i // 2
#         return ans
                

