#
# @lc app=leetcode id=1372 lang=python3
#
# [1372] Longest ZigZag Path in a Binary Tree
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, lastTurn, steps):
            self.ans = max(self.ans, steps)
            if not node:
                return
            if lastTurn == 'left':
                dfs(node.right, 'right', steps + 1)
                dfs(node.left, 'left', 0)
            elif lastTurn == 'right':
                dfs(node.right, 'right', 0)
                dfs(node.left, 'left', steps + 1)
            else:
                dfs(node.left, 'left', 0)
                dfs(node.right, 'right', 0)
        dfs(root, 'none', 0)
        return self.ans
# @lc code=end

