#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 1
        node = head
        while node:
            if length == k:
                kNode = node
            node = node.next
            length += 1
        node = head
        for _ in range(length - k - 1):
            node = node.next
        if node and kNode:
            node.val, kNode.val = kNode.val, node.val
        return head
# @lc code=end
