from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


sol = Solution()
print(sol.increasingTriplet([1, 2, 3, 4, 5]))
print(sol.increasingTriplet([5, 4, 3, 2, 1]))
print(sol.increasingTriplet([2, 1, 5, 0, 4, 6]))
print(sol.increasingTriplet([2, 1, 5, 4, 6]))
print(sol.increasingTriplet([20, 100, 5, 10, 14, 16]))
