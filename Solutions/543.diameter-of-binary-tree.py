#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if node is None:
                return 0
            leftMax, rightMax = dfs(node.left), dfs(node.right)
            self.ans = max(self.ans, leftMax + rightMax)
            return max(leftMax, rightMax) + 1

        dfs(root)
        return self.ans
# @lc code=end
