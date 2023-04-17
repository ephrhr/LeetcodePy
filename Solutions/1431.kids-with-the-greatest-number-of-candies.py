#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#
from typing import List
# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        ans = [False for _ in range(len(candies))]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest:
                ans[i] = True
        return ans
# @lc code=end

