#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = [root]
        ans = []
        while q:
            nq = []
            maxNum = float('-inf')
            for i in range(len(q)):
                node = q[i]
                if node:
                    maxNum = max(maxNum, node.val)
                    nq.append(node.left)
                    nq.append(node.right)
            q = nq
            if q:
                ans.append(int(maxNum))
        return ans

# @lc code=end
