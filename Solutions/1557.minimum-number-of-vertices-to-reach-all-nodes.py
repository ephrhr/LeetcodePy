#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#
from typing import List
from collections import deque
# @lc code=start


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set([t for f, t in edges])
        return [i for i in range(n) if i not in reachable]
# @lc code=end
