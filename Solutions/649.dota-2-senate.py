#
# @lc app=leetcode id=649 lang=python3
#
# [649] Dota2 Senate
#
from collections import deque
# @lc code=start
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        ans = ['Radiant', 'Dire']
        radiant = dire = 0
        banQ = deque()
        lst = []
        n = len(senate)
        for i in range(n):
            s = senate[i]
            lst.append(s)
            if s == 'R': 
                radiant += 1
            else: 
                dire += 1
        while radiant and dire:
            for i in range(n):
                if banQ and lst[i] == banQ[-1]:
                    lst[i] = '#'
                    banQ.pop()
                if lst[i] == 'R':
                    banQ.appendleft('D')
                    dire -= 1
                    if not dire: return ans[0]
                elif lst[i] == 'D':
                    banQ.appendleft('R')
                    radiant -= 1
                    if not radiant: return ans[1]
        return ans[0] if radiant else ans[1]
                    
                    
# @lc code=end

