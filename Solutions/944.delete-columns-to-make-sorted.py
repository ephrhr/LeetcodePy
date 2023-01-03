#
# @lc app=leetcode id=944 lang=python3
#
# [944] Delete Columns to Make Sorted
#
from typing import List
# @lc code=start

# O(mn)


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m, n = len(strs), len(strs[0])
        ans = 0
        for c in range(n):
            for r in range(1, m):
                if strs[r][c] < strs[r - 1][c]:
                    ans += 1
                    break
        return ans
# @lc code=end


# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         n = len(strs[0])
#         ans = 0
#         for i in range(n):
#             last = 'a'
#             for c in strs:
#                 if c[i] < last:
#                     ans += 1
#                     break
#                 last = c[i]
#         return ans
