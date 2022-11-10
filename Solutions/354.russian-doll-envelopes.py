#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
from typing import List
# @lc code=start


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []

        def bSearch(list, value):
            left, right = 0, len(list)
            while left < right:
                mid = (left + right) // 2
                if list[mid] < value:
                    left = mid + 1
                else:
                    right = mid
            return left
        for _, height in envelopes:
            left = bSearch(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)
# @lc code=end
