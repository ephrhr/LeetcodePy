#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        equal, ans = (a | b) ^ c, 0
        for i in range(31):
            mask = 1 << i
            if equal & mask > 0:
                ans += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
        return ans

# @lc code=end
