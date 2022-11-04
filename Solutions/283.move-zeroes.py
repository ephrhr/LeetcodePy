#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List
# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        """
        Do not return anything, modify nums in-place instead.
        """

# @lc code=end
