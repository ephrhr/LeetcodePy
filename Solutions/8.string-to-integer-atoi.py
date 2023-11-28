#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        i = 0
        sign = 1
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return ans

        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        if i == len(s):
            return ans

        while i < len(s) and '0' <= s[i] <= '9':
            ans = ans * 10 + ord(s[i]) - ord('0')
            if ans > 2 ** 31 - 1:
                break
            i += 1
        if sign * ans > 2 ** 31 - 1 or sign * ans < -2 ** 31:
            return sign * (2 ** 31 - 1) if sign == 1 else -2 ** 31
        return int(ans) * sign
# @lc code=end
