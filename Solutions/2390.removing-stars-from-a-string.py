#
# @lc app=leetcode id=2390 lang=python3
#
# [2390] Removing Stars From a String
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for c in s:
            if c != '*': ans.append(c)
            else:
                if ans: ans.pop()
        return ''.join(ans)
# @lc code=end

