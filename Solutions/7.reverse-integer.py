#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(abs(x))[::-1])
        return (-ans if x < 0 else ans) if ans.bit_length() < 32 else 0
# @lc code=end
