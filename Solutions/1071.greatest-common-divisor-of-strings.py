#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
from math import gcd
# @lc code=start


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        return str1[:gcd(len(str1), len(str2))] if str1 + str2 == str2 + str1 else ''
# @lc code=end
