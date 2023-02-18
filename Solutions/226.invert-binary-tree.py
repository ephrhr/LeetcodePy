#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
from typing import Optional
from collections import deque
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        q = deque([root])
        while q:
            nq = deque()
            while q:
                node = q.popleft()
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
                node.left, node.right = node.right, node.left
            q = nq
        return root
# @lc code=end
# DFS
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         def dfs(node: Optional[TreeNode]):
#             if not node:
#                 return
#             dfs(node.left)
#             dfs(node.right)
#             node.left, node.right = node.right, node.left
#         dfs(root)
#         return root

