class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        ans = 0
        maxCount = 0
        l, r = 0, 0
        while r < len(s):
            length = r - l + 1
            count[ord(s[r]) - ord("A")] += 1
            maxCount = max(maxCount, count[ord(s[r]) - ord("A")])
            if length - maxCount > k:
                count[ord(s[l]) - ord("A")] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans


sol = Solution()
print(sol.characterReplacement("AABABBA", 1))
print(sol.characterReplacement("AAAA", 0))
