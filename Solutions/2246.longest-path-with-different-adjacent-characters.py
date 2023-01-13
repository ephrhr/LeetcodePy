#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#
from typing import List
from collections import defaultdict
# @lc code=start


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for end, start in enumerate(parent):
            tree[start].append(end)
        self.ans = 1

        def dfs(node: int):
            max1 = max2 = 0
            for next in tree[node]:
                nextL = dfs(next)
                if s[next] != s[node]:
                    if nextL > max1:
                        max2 = max1
                        max1 = nextL
                    elif nextL > max2:
                        max2 = nextL
            self.ans = max(self.ans, max1 + max2 + 1)
            return max1 + 1
        dfs(0)
        return self.ans
# @lc code=end
