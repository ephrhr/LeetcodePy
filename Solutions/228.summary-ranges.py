#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
from typing import List
# @lc code=start


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start = nums[0]
        ans = []
        for i in range(len(nums)):
            if i == len(nums) - 1 or i < len(nums) - 1 and nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(nums[i]))
                if i < len(nums) - 1:
                    start = nums[i + 1]
        return ans
# @lc code=end
