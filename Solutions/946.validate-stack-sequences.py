#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#
from typing import List
# @lc code=start
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = 0
        for n in pushed:
            stk.append(n)
            while stk and stk[-1] == popped[i]:
                stk.pop()
                i += 1
                 
        return not stk
            
# @lc code=end

