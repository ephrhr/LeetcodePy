#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#
from typing import List
# @lc code=start


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[] for _ in range(len(nums))]
        dp[0].append(nums[0])

        for i in range(1, len(nums)):
            maxSubsetLength = 0
            index = -1
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) > maxSubsetLength:
                    maxSubsetLength = len(dp[j])
                    index = j

            if index != -1:
                dp[i].extend(dp[index])
            dp[i].append(nums[i])

        ans = dp[0]
        for i in range(1, len(dp)):
            if len(ans) < len(dp[i]):
                ans = dp[i]
        return ans
# @lc code=end
