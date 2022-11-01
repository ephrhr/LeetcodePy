class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mp:
                return [mp[diff], i]
            mp[n] = i


sol = Solution()
print(sol.twoSum([2, 7, 11, 13], 9))
print(sol.twoSum([3, 2, 4], 6))
