from tokenize import String
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


sol = Solution()
print(sol.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
print(sol.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
