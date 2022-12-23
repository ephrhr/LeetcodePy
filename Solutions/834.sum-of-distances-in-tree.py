#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#
from typing import List
from collections import defaultdict
# @lc code=start


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        weights, depths, ans = [0]*n, [0]*n, [0]*n
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        def dfs(node, parent, depth):
            ans = 1
            for neib in graph[node]:
                if neib != parent:
                    ans += dfs(neib, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans

        def dfs2(node, parent, w):
            ans[node] = w
            for neib in graph[node]:
                if neib != parent:
                    dfs2(neib, node, w + n - 2*weights[neib])

        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))

        return ans

# @lc code=end
