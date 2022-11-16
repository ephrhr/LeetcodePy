#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
from typing import List
import heapq
import collections
# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        for key, val in mp.items():
            freq[val].append(key)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
# @lc code=end
