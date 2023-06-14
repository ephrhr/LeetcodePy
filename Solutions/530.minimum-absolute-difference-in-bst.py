#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
from typing import Optional


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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = float('-inf')
        self.ans = float('inf')

        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            dfs(node.right)

        dfs(root)
        return self.ans


# @lc code=end
