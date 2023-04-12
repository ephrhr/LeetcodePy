#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = ''
        q = path.split('/')
        stk = []
        for dir in q:
            if dir == '..':
                if stk:
                    stk.pop()
            elif dir == '.' or dir == '':
                continue
            else:
                stk.append(dir)
        
        for dir in stk:
            ans += '/'
            ans += dir
            
        return ans if stk else '/'
# @lc code=end

