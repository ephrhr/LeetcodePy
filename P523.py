from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        map = {0: -1}
        sum = 0
        for i, n in enumerate(nums):
            sum = (sum + n) % k
            if sum in map and i - map[sum] > 1:
                return True
            elif sum not in map:
                map[sum] = i
        return False


sol = Solution()
print(sol.checkSubarraySum([23, 2, 4, 6, 7], 6))
print(sol.checkSubarraySum([23, 2, 6, 4, 7], 6))
print(sol.checkSubarraySum([23, 2, 6, 4, 7], 13))
