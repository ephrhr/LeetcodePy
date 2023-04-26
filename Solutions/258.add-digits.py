#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1
# @lc code=end
# class Solution:
#     def addDigits(self, num: int) -> int:
#         nums = [int(n) for n in str(num)]
#         while len(nums) > 1:
#             nums = [int(n) for n in str(sum(nums))]
#         return sum(nums)

