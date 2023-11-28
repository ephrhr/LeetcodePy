#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List
# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the variable to store the maximum area
        ans = 0

        # Initialize two pointers at the beginning and end of the array
        left = 0
        right = len(height) - 1

        # Continue the loop until the two pointers meet
        while left < right:
            # Calculate the width of the container
            w = right - left

            # Calculate the height of the container (minimum height between the two lines)
            h = min(height[left], height[right])

            # Update the maximum area if the current area is greater
            ans = max(ans, w * h)

            # Move the pointers towards the center, choosing the side with a potentially greater height
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

        # Return the maximum area found
        return ans

# @lc code=end

# This code implements the two-pointer
# approach to find the maximum area between
# vertical lines. The key idea is to start
# with the widest possible container and move
# the pointers towards the center while
# adjusting the height to maximize the
# container's area. The loop continues
# until the two pointers meet.
