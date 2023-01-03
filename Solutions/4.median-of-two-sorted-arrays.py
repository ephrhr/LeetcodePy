#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
from typing import List
# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        k = (m + n + 1) // 2
        l = 0
        r = m
        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                l = m1 + 1
            else:
                r = m1
        m1 = l
        m2 = k - m1
        c1 = max(float('-inf') if m1 <=
                 0 else nums1[m1 - 1], float('-inf') if m2 <= 0 else nums2[m2 - 1])
        if (m + n) % 2 == 1:
            return c1
        c2 = min(float('inf') if m1 >= m else nums1[m1], float(
            'inf') if m2 >= n else nums2[m2])
        return (c1 + c2) / 2
# @lc code=end
