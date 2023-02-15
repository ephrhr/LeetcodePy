#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ans = []
        num_k = deque()
        while k > 0:
            num_k.append(k % 10)
            k //= 10
        carry = 0
        while num or num_k or carry > 0:
            sum = carry
            if num: sum += num.pop()
            if num_k: sum += num_k.popleft()
            carry = 0 if sum < 10 else sum // 10
            sum = sum % 10
            ans.append(sum)
        return ans[::-1]
# @lc code=end
# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         ans = []
#         a = 0
#         mul = 1
#         for i in range(len(num) - 1, -1, -1):
#             a += num[i] * mul
#             mul *= 10
#         sum = a + k
#         while sum > 0:
#             ans.append(sum % 10)
#             sum //= 10
#         return ans[::-1]

