from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(2, len(nums), 1):
            a, b, c = nums[i], nums[i - 1], nums[i - 2]
            if a + b > c:
                return a + b + c
        return 0


sol = Solution()
print(sol.largestPerimeter([2, 1, 2, 3]))
print(sol.largestPerimeter([1, 1, 2]))
print(sol.largestPerimeter([2, 1, 2]))
print(sol.largestPerimeter([3, 6, 2, 3]))
