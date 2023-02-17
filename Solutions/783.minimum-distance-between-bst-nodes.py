#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node, low, high):
            if not node:
                return high - low
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)
            return min(left, right)
        return dfs(root, -100001, 100001)
                
# @lc code=end
# Store sorted list from in-order traversal
# class Solution:
#     def minDiffInBST(self, root: Optional[TreeNode]) -> int:
#         ans = 100001
#         nums = []
#         def dfs(node: Optional[TreeNode]):
#             if not node:
#                 return
#             dfs(node.left)
#             nums.append(node.val)
#             dfs(node.right)

#         dfs(root)
#         for i in range(1, len(nums)):
#             ans = min(ans, nums[i] - nums[i - 1])
#         return ans

