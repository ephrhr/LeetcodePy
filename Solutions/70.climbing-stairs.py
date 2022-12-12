#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 0, 1]
        for _ in range(n):
            dp[2] = dp[0] + dp[1]
            dp[1], dp[0] = dp[0], dp[2]
        return dp[2]
# @lc code=end
