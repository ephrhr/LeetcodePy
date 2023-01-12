#
# @lc app=leetcode id=1519 lang=python3
#
# [1519] Number of Nodes in the Sub-Tree With the Same Label
#
from typing import List
from collections import defaultdict, Counter
# @lc code=start


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, parent: int):
            count = Counter(labels[node])
            for next in graph[node]:
                if next != parent:
                    count += dfs(next, node)
            ans[node] = count[labels[node]]
            return count
        dfs(0, -1)
        return ans
# @lc code=end
