#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        self.memo = [-1] * (n + 1)

        def dp(n: int):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if self.memo[n] != -1:
                return self.memo[n]

            ans = float('-inf')
            for i in range(1, n + 1):
                ans = max(ans, i * max(dp(n - i), n - i))
            self.memo[n] = ans
            return ans

        return dp(n)
# @lc code=end
