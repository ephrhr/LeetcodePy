#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        def dfs(node):
            if node is None:
                return 0
            leftMaxSum = max(0, dfs(node.left))
            rightMaxSum = max(0, dfs(node.right))
            currSum = node.val + leftMaxSum + rightMaxSum
            self.maxSum = max(self.maxSum, currSum)
            return max(leftMaxSum, rightMaxSum) + node.val
        dfs(root)
        return self.maxSum
# @lc code=end
