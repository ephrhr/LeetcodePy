#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # if n >= k + maxPts, the probability of i >= k and i <= n is 1
        if k == 0 or k + maxPts <= n:
            return 1

        # we don't need to calculate the probability after n
        # because the problem asks for the probability of k <= i <= n
        dp = [0] * (n + 1)

        # the probability of 0 points is 1 because the game starts with 0
        dp[0] = 1
        s = 1
        for i in range(1, n + 1):
            # dp[i] = probability of getting i points
            dp[i] = s / maxPts

            # add up if i + 1 <= k
            if i < k:
                s += dp[i]

            # minus if i + 1 > maxPts
            if i - maxPts >= 0:
                s -= dp[i - maxPts]

        # return probability of k <= i <= n
        return sum(dp[k:])
# @lc code=end
