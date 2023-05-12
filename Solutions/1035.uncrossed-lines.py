#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#
from typing import List
# @lc code=start


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        memo = [0] * (n + 1)
        for i in range(m):
            for j in range(n)[::-1]:
                if nums1[i] == nums2[j]:
                    memo[j + 1] = memo[j] + 1
            for j in range(n):
                memo[j + 1] = max(memo[j + 1], memo[j])
        return memo[n]
# @lc code=end
