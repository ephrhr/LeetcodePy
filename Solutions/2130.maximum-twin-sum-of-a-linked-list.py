#
# @lc app=leetcode id=2130 lang=python3
#
# [2130] Maximum Twin Sum of a Linked List
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

# SC: O(1)


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        ans = float('-inf')
        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        while slow:
            ans = max(ans, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        return ans
# @lc code=end

# SC: O(n)
# class Solution:
#     def pairSum(self, head: Optional[ListNode]) -> int:
#         slow = fast = head
#         twins = []

#         while fast and fast.next:
#             twins.append(slow.val)
#             slow = slow.next
#             fast = fast.next.next
#         for i in range(len(twins) - 1, -1, -1):
#             twins[i] += slow.val
#             slow = slow.next
#         return max(twins)
