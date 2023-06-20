#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#
from typing import List
# @lc code=start


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        n = len(nums)
        diameter = k * 2 + 1
        if n < diameter:
            return [-1] * n
        ans = [-1] * k
        nSum = sum(nums[:diameter - 1])
        for r in range(diameter - 1, n):
            nSum += nums[r]
            ans.append(nSum // diameter)
            nSum -= nums[r - diameter + 1]
        for _ in range(n - k, n):
            ans.append(-1)
        return ans
# @lc code=end
