#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#
from typing import List
# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min capacity = max weight of the cargos
        # max capacity = sum of weight of the cargos
        left, right = max(weights), sum(weights)
        while left < right:
            mid, needDays, capacity = (left + right) // 2, 1, 0
            
            # try to ship all the cargos and calculate how many days needed
            for w in weights:
                if capacity + w > mid:
                    needDays += 1
                    capacity = 0
                capacity += w
                
            # need bigger capacity
            if needDays > days: 
                left = mid + 1
                
            # capacity can be smaller
            else: 
                right = mid
            
        return left
        
# @lc code=end

