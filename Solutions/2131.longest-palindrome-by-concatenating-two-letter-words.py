#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#
from typing import List, DefaultDict
# @lc code=start


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        mp = DefaultDict(int)
        unpaired = ans = 0
        for word in words:
            if word[0] == word[1]:
                if mp[word] > 0:
                    unpaired -= 1
                    mp[word] -= 1
                    ans += 4
                else:
                    mp[word] += 1
                    unpaired += 1
            else:
                if mp[word[::-1]] > 0:  # reversed word
                    ans += 4
                    mp[word[::-1]] -= 1
                else:
                    mp[word] += 1
        if unpaired > 0:
            ans += 2
        return ans


# @lc code=end
sol = Solution()
print(sol.longestPalindrome(["lc", "cl", "gg"]))
# mp = Map<str, int>
