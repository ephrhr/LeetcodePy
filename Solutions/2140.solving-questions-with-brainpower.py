#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#
from typing import List
# @lc code=start


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        memo = [q[0] for q in questions]
        for i in range(n - 2, -1, -1):
            if i + questions[i][1] + 1 < n:
                memo[i] += memo[i + questions[i][1] + 1]
            memo[i] = max(memo[i], memo[i + 1])
        return memo[0]
# @lc code=end
