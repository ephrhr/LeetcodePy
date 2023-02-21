#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
from typing import List
# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid % 2 == 0 and nums[mid + 1] == nums[mid]):
                left = mid + 1
            else:
                right = mid
        return nums[left]
        
# @lc code=end
# Two pointers, TC: O(n)
# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         left, right = 0, len(nums) - 1
#         while left < len(nums) - 1 and right > 0:
#             if nums[left] != nums[left + 1]:
#                 return nums[left]
#             if nums[right] != nums[right - 1]:
#                 return nums[right]
#             left += 2
#             right -= 2
#         return -1 if len(nums) > 1 else nums[0]

