#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: 
                while head != slow:
                    head, slow = head.next, slow.next
                return head
        return None

# @lc code=end

# SC: O(n)
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         st = set()
#         while head and head.next:
#             st.add(head)
#             if head.next in st:
#                 return head.next
#             head = head.next
#         return None

