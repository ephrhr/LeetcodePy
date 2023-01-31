#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 0 if n == 0 else 1
        oneStepBefore = 1
        twoStepBefore = 1
        threeStepBefore = 0
        ans = 2
        for _ in range(3, n):
            threeStepBefore = twoStepBefore
            twoStepBefore = oneStepBefore
            oneStepBefore = ans
            ans = oneStepBefore + twoStepBefore + threeStepBefore
        return ans
# @lc code=end
