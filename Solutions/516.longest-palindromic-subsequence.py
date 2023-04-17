#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = [0] * n
        for i in range(n - 1, -1, -1):
            memo[i] = 1
            prev = 0
            for j in range(i + 1, n):
                cur = memo[j]
                if s[i] == s[j]:
                    memo[j] = prev + 2
                else:
                    memo[j] = max(memo[j], memo[j - 1])
                prev = cur
        return memo[n - 1]
# @lc code=end

