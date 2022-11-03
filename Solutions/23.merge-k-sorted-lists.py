#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
from typing import List, Optional
# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        dummy = p = ListNode()
        pq = [(head.val, i, head) for i, head in enumerate(lists) if head]
        heapq.heapify(pq)
        while pq:
            val, i, node = pq[0]
            if node.next:
                heapq.heapreplace(pq, (node.next.val, i, node.next))
            else:
                heapq.heappop(pq)
            p.next = node
            p = p.next
        return dummy.next

# @lc code=end
