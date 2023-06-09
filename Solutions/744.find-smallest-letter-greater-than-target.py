#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
from typing import List
# @lc code=start


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        l, r = 0, len(letters) - 1
        while l < r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m
            else:
                l = m + 1

        return letters[r] if letters[r] > target else letters[0]
# @lc code=end

# if letters is unsorted

# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#         st = set(letters)
#         n = ord('z') + 1
#         for i in range(ord(target) + 1, n):
#             if chr(i) in st:
#                 return chr(i)

#         return letters[0]
