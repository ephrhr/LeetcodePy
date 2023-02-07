#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
from typing import List
# @lc code=start


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = current = bCount = a = b = 0
        for fruit in fruits:
            current = current + 1 if fruit in (a, b) else bCount + 1
            bCount = bCount + 1 if fruit == b else 1
            if b != fruit:
                a, b = b, fruit
            ans = max(ans, current)
        return ans
# @lc code=end
# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         memo = [1 for _ in range(len(fruits))]
#         for i in range(len(fruits)):
#             st = set()
#             st.add(fruits[i])
#             j = i + 1
#             while j < len(fruits) and len(st) <= 2:
#                 if len(st) == 2 and fruits[j] not in st:
#                     break
#                 st.add(fruits[j])
#                 memo[i] += 1
#                 j = j + 1
#         return max(memo)
