#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
from typing import List, Optional
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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mp = {v: i for i, v in enumerate(inorder)}
        self.mid = len(postorder) - 1
        def build(start, end):
            if start > end:
                return None
            node = TreeNode(postorder[self.mid])
            right = mp[node.val] + 1
            self.mid -= 1
            left = mp[node.val] - 1
            node.right = build(right, end)
            node.left = build(start, left)
            return node
        return build(0, self.mid)
# @lc code=end

# dfs():
#     ..
#     dfs(left)
#     ..in-order
#     dfs(right)
#     ..post-order
# in-order: left -> node -> right
# post-order: left -> right -> node

# Solution idea:
# handle orders at recursion: node -> right -> left
# map node's value to index in in-order list in a hashmap instead of searching in in-order list
# making each resucion can fetch node's value in O(1)