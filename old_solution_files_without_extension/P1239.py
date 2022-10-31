from typing import List


# DP & bit manipulation
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for word in arr:
            if len(set(word)) < len(word):
                continue
            word = set(word)
            for c in dp[:]:
                if word & c:
                    continue
                dp.append(word | c)
        return max(len(word) for word in dp)


sol = Solution()
print(sol.maxLength(["un", "iq", "ue"]))
