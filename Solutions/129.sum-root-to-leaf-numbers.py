#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
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
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], num=''):
            if node:
                num += str(node.val)
            if not node.left and not node.right:
                self.ans += int(num)
            if node.left:
                dfs(node.left, num)
            if node.right:
                dfs(node.right, num)
        dfs(root)
        return self.ans
# @lc code=end

