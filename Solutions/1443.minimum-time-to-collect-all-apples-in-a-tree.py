#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#
from typing import List
from collections import defaultdict
# @lc code=start


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        paths = defaultdict(list)
        for a, b in edges:
            paths[a].append(b)
            paths[b].append(a)

        self.ans = 0
        visited = set()

        def dfs(node):
            found = False
            if node in visited:
                return
            visited.add(node)
            for next in paths[node]:
                if dfs(next):
                    found = True
                    self.ans += 2
            return found or hasApple[node]
        dfs(0)
        return self.ans
# @lc code=end
