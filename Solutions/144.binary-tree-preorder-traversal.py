#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [] if root is None else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
# @lc code=end
# class Solution:
#     def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         if root is None:
#             return ans
#         ans += [root.val]
#         ans += self.preorderTraversal(root.left)
#         ans += self.preorderTraversal(root.right)
#         return ans
