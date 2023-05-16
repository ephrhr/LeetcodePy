#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head
# @lc code=end
