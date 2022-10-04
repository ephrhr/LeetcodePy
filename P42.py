from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                ans += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                ans += rMax - height[r]
        return ans


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
