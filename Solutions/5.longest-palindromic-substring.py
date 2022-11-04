#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findPalindrome(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1: r]
        ans = ''
        for i in range(len(s)):
            odd = findPalindrome(i, i)
            even = findPalindrome(i, i + 1)
            ans = odd if len(odd) > len(ans) else ans
            ans = even if len(even) > len(ans) else ans
        return ans


# @lc code=end
