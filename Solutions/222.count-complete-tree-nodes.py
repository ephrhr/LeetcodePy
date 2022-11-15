#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getDepth(node: Optional[TreeNode]):
            if not node:
                return 0
            return 1 + getDepth(node.left)
        lDepth = getDepth(root.left)
        rDepth = getDepth(root.right)
        if lDepth == rDepth:
            return 2 ** lDepth + self.countNodes(root.right)
        else:
            return 2 ** rDepth + self.countNodes(root.left)
# @lc code=end

# O(log(n) ^ 2)
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         def getDepth(node: Optional[TreeNode]):
#             if not node:
#                 return 0
#             return 1 + getDepth(node.left)
#         lDepth = getDepth(root.left)
#         rDepth = getDepth(root.right)
#         if lDepth == rDepth:
#             return 2 ** lDepth + self.countNodes(root.right)
#         else:
#             return 2 ** rDepth + self.countNodes(root.left)

# BFS O(n)
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         return 0 if not root else 1 + self.countNodes(root.left) + self.countNodes(root.right)

# BFS O(n)
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         q = [root]
#         ans = 0
#         while len(q):
#             nq = []
#             while len(q):
#                 node = q.pop()
#                 if node:
#                     ans += 1
#                     nq.append(node.left)
#                     nq.append(node.right)
#             q = nq
#         return ans
