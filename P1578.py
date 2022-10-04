class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        ans = left = 0
        for i in range(1, len(colors)):
            if colors[left] == colors[i]:
                ans += min(neededTime[left], neededTime[i])
                if neededTime[left] > neededTime[i]:
                    continue
            left = i
        return ans


sol = Solution()
print(sol.minCost("abaac", [1, 2, 3, 4, 5]))
print(sol.minCost("abc", [1, 2, 3]))
print(sol.minCost("aabaa", [1, 2, 3, 4, 1]))
print(sol.minCost("aaabbbabbbb",
      [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1]))
