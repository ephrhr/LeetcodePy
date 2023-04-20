#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
# BFS
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0, 0)])
        curLevel = left = ans = 0
        while q:
            (node, level, pos) = q.pop()
            if node.left:
                q.appendleft((node.left, level + 1, pos * 2))
            if node.right:
                q.appendleft((node.right, level + 1, pos * 2 + 1))
            if curLevel != level:
                curLevel = level
                left = pos
            ans = max(ans, pos - left + 1)
        return ans
# @lc code=end
# DFS
# class Solution:
#     def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         left = {}
#         self.ans = 0
#         def dfs(node, level, pos):
#             if not node: return
#             if level not in left: left[level] = pos
#             self.ans = max(self.ans, pos - left[level] + 1)
#             dfs(node.left, level + 1, pos * 2)
#             dfs(node.right, level + 1, pos * 2 + 1)
#         dfs(root, 0, 0)
#         return self.ans

