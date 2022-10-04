from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        for k in st:
            if (k - 1) not in st:
                count = 1
                n = k
                while (n + count) in st:
                    count += 1
                ans = max(ans, count)
        return ans


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(sol.longestConsecutive([9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]))
