#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#
from typing import List
# @lc code=start


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        ans = [0] * len(arr)
        stack = [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]:
                stack.pop()
            j = stack[-1]
            ans[i] = ans[j] + (i - j) * arr[i]
            stack.append(i)
        return sum(ans) % (10**9 + 7)
# @lc code=end
