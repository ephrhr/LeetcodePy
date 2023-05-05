#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        ans = 0
        for c in s[:k]:
            if c in vowels:
                ans += 1
        count = ans
        for r in range(k, len(s)):
            if s[r - k] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            ans = max(ans, count)
        return ans
# @lc code=end

