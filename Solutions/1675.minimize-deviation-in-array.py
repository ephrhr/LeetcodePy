#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, [n / (n & -n), n])
        ans = float('inf')
        ma = max(n for n, o in pq)
        while len(pq) == len(nums):
            n, o = heapq.heappop(pq)
            ans = min(ans, ma - n)
            if n % 2 == 1 or n < o:
                ma = max(ma, n * 2)
                heapq.heappush(pq, [n * 2, o])
        return int(ans)
# @lc code=end

