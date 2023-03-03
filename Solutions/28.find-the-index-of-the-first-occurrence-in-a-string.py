#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        n, m = len(haystack), len(needle)
        def lpsBuilder():
            i, j = 1, 0
            lps = [0] * m
            while i < m:
                if needle[i] == needle[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = lps[j - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        lps = lpsBuilder()
        i, j = 0, 0
        while n - i >= m - j:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            if j == m:
                return i - j
            elif i < n and haystack[i] != needle[j]:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
# @lc code=end

# KMP Algorithm: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/

