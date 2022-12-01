#
# @lc app=leetcode id=1704 lang=python3
#
# [1704] Determine if String Halves Are Alike
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        i, j = 0, len(s) // 2
        a, b = 0, 0
        while j < len(s):
            a += s[i] in vowels
            b += s[j] in vowels
            i += 1
            j += 1
        return a == b
# @lc code=end
