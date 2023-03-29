#
# @lc app=leetcode id=1402 lang=python3
#
# [1402] Reducing Dishes
#
from typing import List
# @lc code=start
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        ans = sum((n - i) * satisfaction[i] for i in range(n))
        while n > 0 and satisfaction[-1] < 0:
            v = sum(satisfaction)
            satisfaction.pop()
            n = len(satisfaction)
            if v > 0: return ans
            ans -= v
        return max(0, ans)
# @lc code=end
# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort(reverse=True)
#         n = len(satisfaction)
#         memo = [0]
#         memo.append(sum((n - i) * satisfaction[i] for i in range(n)))
#         while n > 0 and satisfaction[-1] < 0:
#             v = sum(satisfaction)
#             satisfaction.pop()
#             n = len(satisfaction)
#             memo.append(memo[-1] - v)
#         return max(memo)

