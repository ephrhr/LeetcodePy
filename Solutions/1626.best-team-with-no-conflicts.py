#
# @lc app=leetcode id=1626 lang=python3
#
# [1626] Best Team With No Conflicts
#
from typing import List
from bisect import bisect_right
# @lc code=start


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        visited = [players[0][1]]
        memo = [players[0][1]]
        ans = players[0][1]
        for i in range(1, len(players)):
            score = players[i][1]
            index = bisect_right(visited, score)
            curr = max(memo[:index]) + score if index else score
            ans = max(ans, curr)
            visited.insert(index, score)
            memo.insert(index, curr)
        return ans

# @lc code=end
# class Solution:
#     def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
#         n = len(ages)
#         memo = [0] * n
#         ans = 0
#         tmp = []
#         for i in range(len(scores)):
#             tmp.append([-ages[i], -scores[i]])
#         tmp.sort()
#         for i in range(n):
#             for j in range(i, -1, -1):
#                 if -tmp[i][1] <= -tmp[j][1]:
#                     memo[i] = max(memo[i], memo[j] - tmp[i][1])
#             ans = max(ans, memo[i])
#         return ans
