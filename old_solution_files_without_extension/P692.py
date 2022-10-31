import collections
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map = collections.Counter(words)
        return heapq.nsmallest(k, map, key=lambda word: (-map[word], word))


sol = Solution()
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
