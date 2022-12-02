#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#
from collections import Counter
# @lc code=start


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) and set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())
# @lc code=end

# ""abbzzca"\n"babzzcz""

# word1 = "abbzzca", word2 = "babzzcz"
# 1. len(word1) == len(word2)

# mp1 = {a:2, b:2, c:1, z:2}
# mp2 = {a:1, b:2, c:1, z:3}
# 2. mp1.keys() == mp2.keys() => set(word1) == set(word2)

# count1 = { 1:1, 2:3 }
# count2 = { 1:2, 2:1, 3:1}
# 3. count1 != count2 ==> return False
