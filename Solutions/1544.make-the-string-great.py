#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        ans = []
        for c in s:
            if not ans:
                ans.append(c)
            elif ans[-1].isupper() and ans[-1].lower() == c:
                ans.pop()
            elif ans[-1].islower() and ans[-1].upper() == c:
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)
# @lc code=end
