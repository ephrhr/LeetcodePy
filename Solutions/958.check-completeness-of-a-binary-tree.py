#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
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
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        includeNull = False
        while q:
            nq = deque()
            while q:
                node = q.pop()
                if not node:
                    includeNull = True
                    continue
                if includeNull:
                    return False
                nq.appendleft(node.left)
                nq.appendleft(node.right)
            q = nq
        return True
# @lc code=end

