#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
from collections import Counter
# @lc code=start


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        match = 0
        for i in range(26):
            match += 1 if s1Count[i] == s2Count[i] else 0
        l, r = 0, len(s1)
        while r < len(s2):
            if match == 26:
                return True

            i = ord(s2[r]) - ord('a')
            s2Count[i] += 1
            if s1Count[i] == s2Count[i]:
                match += 1
            elif s1Count[i] + 1 == s2Count[i]:
                match -= 1

            i = ord(s2[l]) - ord('a')
            s2Count[i] -= 1
            if s1Count[i] == s2Count[i]:
                match += 1
            elif s1Count[i] - 1 == s2Count[i]:
                match -= 1

            l += 1
            r += 1
        return match == 26

# @lc code=end
