#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for c in s:
            if ans and ans[-1] == c:
                ans.pop()
            else:
                ans.append(c)
        return ''.join(ans)

# @lc code=end
