#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize variables to store the result, current index, and sign
        ans = 0
        i = 0
        sign = 1

        # Skip leading whitespaces
        while i < len(s) and s[i] == ' ':
            i += 1
        # Return 0 if the string is empty after removing whitespaces
        if i == len(s):
            return ans

        # Determine the sign (positive or negative)
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        # Return 0 if the string is empty after determining the sign
        if i == len(s):
            return ans

        # Convert consecutive digits into an integer
        while i < len(s) and '0' <= s[i] <= '9':
            ans = ans * 10 + ord(s[i]) - ord('0')
            # Break if the result exceeds the 32-bit signed integer range
            if ans > 2 ** 31 - 1:
                break
            i += 1

        # Clamp the result to the 32-bit signed integer range
        if sign * ans > 2 ** 31 - 1 or sign * ans < -2 ** 31:
            return sign * (2 ** 31 - 1) if sign == 1 else -2 ** 31

        # Return the final result
        return int(ans) * sign

# @lc code=end

# This code implements the myAtoi function
# according to the specified algorithm,
# handling leading whitespaces, determining
# the sign, converting digits into an integer,
# and clamping the result to the 32-bit signed
# integer range.
