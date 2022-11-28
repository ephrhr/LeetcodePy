#
# @lc app=leetcode id=2225 lang=python3
#
# [2225] Find Players With Zero or One Losses
#
from typing import List
import collections
# @lc code=start


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = [], []
        loseCount = collections.defaultdict(int)
        for winner, loser in matches:
            loseCount[winner] = loseCount[winner]
            loseCount[loser] += 1
        for key, value in loseCount.items():
            # player that have not lost any matches
            if value == 0:
                winners.append(key)
            # player that have lost exactly one match
            if value == 1:
                losers.append(key)
        return [sorted(winners), sorted(losers)]
# @lc code=end
