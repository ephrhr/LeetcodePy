#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        hashSet = set()
        start = 0
        end = 1
        ans = 0
        hashSet.add(s[start])
        while end < len(s):
            while s[end] in hashSet and start < end:
                ans = max(ans, end - start)
                hashSet.remove(s[start])
                start += 1
                hashSet.add(s[start])
            hashSet.add(s[end])
            end += 1
        ans = max(ans, end - start)
        return ans
# @lc code=end
