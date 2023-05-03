#
# @lc app=leetcode id=2215 lang=python3
#
# [2215] Find the Difference of Two Arrays
#
from typing import List
# @lc code=start
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        st1, st2 = set(nums1), set(nums2)
        ans = [[],[]]
        for n in st1:
            if n not in st2:
                ans[0].append(n)
        for n in st2:
            if n not in st1:
                ans[1].append(n)
        return ans
        
# @lc code=end

