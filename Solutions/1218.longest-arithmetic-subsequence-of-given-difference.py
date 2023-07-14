#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#
from typing import List
# @lc code=start


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        dp = {}
        for num in arr:
            previous = dp.get(num - difference, 0)
            dp[num] = previous + 1
            ans = max(ans, dp[num])
        return ans
# @lc code=end
