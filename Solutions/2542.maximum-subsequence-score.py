#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#
from typing import List
import heapq
# @lc code=start


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pq = []
        count = ans = 0
        for n1, n2 in sorted(zip(nums1, nums2), key=lambda x: -x[1]):
            heapq.heappush(pq, n1)
            count += n1
            if len(pq) > k:
                count -= heapq.heappop(pq)
            if len(pq) == k:
                ans = max(ans, count * n2)
        return ans
# @lc code=end
