#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
from typing import List
import heapq
# @lc code=start


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        ans = []
        visited = set()

        minHeap = [(nums1[0] + nums2[0], (0, 0))]
        visited.add((0, 0))

        while k > 0 and minHeap:
            s, (i, j) = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(minHeap, (nums1[i + 1] + nums2[j], (i + 1, j)))
                visited.add((i + 1, j))

            if j + 1 < m and (i, j + 1) not in visited:
                heapq.heappush(minHeap, (nums1[i] + nums2[j + 1], (i, j + 1)))
                visited.add((i, j + 1))
            k = k - 1

        return ans
# @lc code=end

# class Solution:
#     def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
#         pq = []
#         for u in nums1:
#             for v in nums2:
#                 heapq.heappush(pq, (u + v, u, v))

#         ans = []
#         while len(ans) < k and len(pq):
#             s, u, v = heapq.heappop(pq)
#             ans.append([u, v])
#         return ans
