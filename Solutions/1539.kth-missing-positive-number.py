#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
from typing import List
# @lc code=start
# O(log(n))
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left ,right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] - 1 - mid < k:
                left = mid + 1
            else:
                right = mid
        return left + k
# @lc code=end
# O(n)
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         i, j = 0, 0
#         ans = 0
#         while i != k:
#             ans += 1
#             if j < len(arr) and ans == arr[j]:
#                 j += 1
#             else:
#                 i += 1
#         return ans

