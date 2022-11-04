#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List
# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
# @lc code=end
