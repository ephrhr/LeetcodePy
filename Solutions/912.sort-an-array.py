#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
from typing import List
# @lc code=start
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            n, m = len(left), len(right)
            sub, i ,j = [], 0, 0
            while i < n and j < m:
                if left[i] <= right[j]:
                    sub.append(left[i])
                    i = i + 1
                else:
                    sub.append(right[j])
                    j = j + 1
            return sub + (right[j:] if i == n else left[i:])
        n = len(nums)
        if n == 1:
            return nums
        left, right = self.sortArray(nums[:n // 2]), self.sortArray(nums[n // 2:])
        return merge(left, right)
# @lc code=end

