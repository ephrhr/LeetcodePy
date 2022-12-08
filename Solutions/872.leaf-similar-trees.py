#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return []
            elif not node.left and not node.right:
                return [node.val]
            return dfs(node.left) + dfs(node.right)
        return dfs(root1) == dfs(root2)
# @lc code=end
