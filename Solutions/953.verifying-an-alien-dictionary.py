#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#
from typing import List
# @lc code=start


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = dict()
        for i, c in enumerate(order):
            orderMap[c] = i
        for i in range(1, len(words)):
            prev = words[i - 1]
            curr = words[i]
            for j in range(len(prev)):
                if j > len(curr) - 1 or orderMap[prev[j]] > orderMap[curr[j]]:
                    return False
                elif orderMap[prev[j]] < orderMap[curr[j]]:
                    break
        return True


# @lc code=end
