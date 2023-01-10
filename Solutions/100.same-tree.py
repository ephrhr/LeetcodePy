#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        elif not p and not q:
            return True
        else:
            return False
# @lc code=end
