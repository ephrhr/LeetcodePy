#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        maxSum = root.val
        level = 1
        ans = 1
        while q:
            nq = deque()
            levelSum = 0
            while q:
                node = q.pop()
                levelSum += node.val
                if node.left:
                    nq.appendleft(node.left)
                if node.right:
                    nq.appendleft(node.right)
            if maxSum < levelSum:
                maxSum = levelSum
                ans = level
            q = nq
            level += 1
        return ans
# @lc code=end
