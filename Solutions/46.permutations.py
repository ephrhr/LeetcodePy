#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans)
        return ans

    def backtrack(self, nums, track, ans) -> None:
        if not nums:
            ans.append(track)
        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i + 1:], track + [nums[i]], ans)
# @lc code=end
