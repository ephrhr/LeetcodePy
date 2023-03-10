#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
from typing import Optional
import random
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

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        n = 0
        node, ans = self.head, self.head.val
        while node:
            if random.randint(0, n) == 0:
                ans = node.val
            node = node.next
            n += 1
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

# SC: O(n)
# class Solution:

#     def __init__(self, head: Optional[ListNode]):
#         self.vals = []
#         while head:
#             self.vals.append(head.val)
#             head = head.next

#     def getRandom(self) -> int:
#         return self.vals[random.randint(0, len(self.vals) - 1)]