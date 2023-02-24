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
        for num in nums:
            # (num & -num) returns the lowest bit of num (even)
            # num / (num & -num) returns the samllest odd number that can divide num
            heapq.heappush(pq, [num / (num & -num), num])
        ans = float('inf')
        maxn = max(num for num, origin in pq)
        while len(pq) == len(nums):
            num, origin = heapq.heappop(pq)
            ans = min(ans, maxn - num)
            if num % 2 == 1 or num < origin:
                maxn = max(maxn, num * 2)
                heapq.heappush(pq, [num * 2, origin])
        return int(ans)
# @lc code=end

