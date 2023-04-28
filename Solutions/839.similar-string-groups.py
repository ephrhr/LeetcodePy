#
# @lc app=leetcode id=839 lang=python3
#
# [839] Similar String Groups
#
from typing import List
# @lc code=start
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def isSimilar(s1, s2):
            if s1 == s2: return True
            diff = 0
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                if diff > 2: return False
            return diff == 2
        
        def dfs(index):
            s = strs[index]
            strs[index] = None
            for i in range(len(strs)):
                if strs[i] and isSimilar(strs[i], s):
                    dfs(i)
        
        if len(strs) < 2: return len(strs)
        ans = 0
        for i in range(len(strs)):
            if strs[i]:
                ans += 1
                dfs(i)
        return ans
# @lc code=end

