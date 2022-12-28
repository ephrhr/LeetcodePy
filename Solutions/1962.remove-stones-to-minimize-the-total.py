#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#
from typing import List
from collections import deque
from heapq import heapreplace, heapify
# @lc code=start


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = [-x for x in piles]
        heapify(pq)
        for _ in range(k):
            heapreplace(pq, pq[0] // 2)
        return -sum(pq)
# @lc code=end


# First came out solution
# class Solution:
#     def minStoneSum(self, piles: List[int], k: int) -> int:
#         piles = sorted(piles)
#         tmp = deque()
#         while k > 0:
#             if len(piles) > 1:
#                 if piles[-1] < piles[-2]:
#                     tmp.append(piles.pop())
#             if tmp and piles[-1] < tmp[0]:
#                 piles.append(tmp.popleft())
#             elif piles[-1] == 1:
#                 break
#             targetFloor = piles[-1] // 2
#             piles[-1] -= targetFloor
#             k -= 1
#         for _ in range(len(tmp)):
#             piles.append(tmp.pop())
#         return sum(piles)
