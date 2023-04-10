#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        
        bracketPair = {')':'(', ']':'[', '}':'{'}
        stk = []
        
        for c in s:
            if c in bracketPair:
                if stk and bracketPair[c] == stk[-1]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
                
        return not stk
# @lc code=end

