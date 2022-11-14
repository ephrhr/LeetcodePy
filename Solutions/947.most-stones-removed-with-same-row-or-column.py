#
# @lc app=leetcode id=947 lang=python3
#
# [947] Most Stones Removed with Same Row or Column
#
from typing import List
# @lc code=start


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in stones:
            union(i, ~j)
        return len(stones) - len({find(x) for x in UF})
# @lc code=end
