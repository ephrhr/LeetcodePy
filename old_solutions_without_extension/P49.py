import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return result.values()


sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
