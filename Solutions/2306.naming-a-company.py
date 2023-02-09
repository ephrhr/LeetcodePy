#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        count = defaultdict(set)
        for word in ideas:
            count[word[0]].add(hash(word[1:]))
        ans = 0
        for i, set_i in count.items():
            for j, set_j in count.items():
                if i >= j: continue
                same = len(set_i & set_j)
                ans += (len(set_i) - same) * (len(set_j) - same)
        return ans * 2
# @lc code=end

# Naive Solution (TLE)
# class Solution:
#     def distinctNames(self, ideas: List[str]) -> int:
#         st = set(ideas)
#         st_2 = set()
#         ans = 0
#         n = len(ideas)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if ideas[i][0] == ideas[j][0]:
#                     continue
#                 firstWord = ideas[j][0] + ideas[i][1:]
#                 secondWord = ideas[i][0] + ideas[j][1:]
#                 name = firstWord + ' ' + secondWord
#                 reversedName = secondWord + ' ' + firstWord
#                 if firstWord not in st and secondWord not in st and name not in st_2 and reversedName not in st_2:
#                     ans += 2
#                     st_2.add(name)
#                     st_2.add(reversedName)
#         return ans

