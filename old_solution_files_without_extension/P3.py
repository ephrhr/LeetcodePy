class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        st = set()
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[i - len(st)])
            st.add(s[i])
            ans = max(ans, len(st))
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
