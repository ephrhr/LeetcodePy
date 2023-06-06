#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#
from typing import List
# @lc code=start

# TC: O(n), SC: O(n)


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ma, mi = max(arr), min(arr)
        n = len(arr)
        st = set(arr)
        if (ma - mi) % (n - 1):
            return False
        diff = (ma - mi) // (n - 1)
        for i in arr:
            if i != ma and i + diff not in st:
                return False
        return True
# @lc code=end

# TC: O(nlogn), SC: O(1)
# class Solution:
#     def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
#         arr.sort()
#         diff = arr[1] - arr[0]
#         start = arr[1]
#         for n in arr[2:]:
#             start += diff
#             if start != n:
#                 return False
#         return True
