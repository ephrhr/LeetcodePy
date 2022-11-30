#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#
from typing import List
import collections
# @lc code=start


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = collections.Counter(arr)
        return len(mp) == len(set(mp.values()))
# @lc code=end
