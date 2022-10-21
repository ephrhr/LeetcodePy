from typing import List
import collections


# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         mp = collections.Counter(nums)
#         for i in range(0, len(nums)):
#             if mp[nums[i]] > 1:
#                 j = i + k if i < len(nums) - k else len(nums) - 1
#                 while i < j < len(nums):
#                     if nums[i] == nums[j]:
#                         return True
#                     j -= 1
#         return False


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True
            seen.add(num)
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3))
print(sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
