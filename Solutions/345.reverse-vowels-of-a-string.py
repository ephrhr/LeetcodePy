#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start

# stack
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = [c for c in s if c in vowels]
        ans = ''
        for c in s:
            if c in vowels:
                ans += stack.pop()
            else:
                ans += c
        return ans

# @lc code=end

# 2 pointers
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         left, right = 0, len(s) - 1
#         s = list(s)
#         while left < right:
#             if s[left] in vowels and s[right] in vowels:
#                 s[left], s[right] = s[right], s[left]
#                 left += 1
#                 right -= 1
#             elif s[left] not in vowels:
#                 left += 1
#             else:
#                 right -= 1
#         return ''.join(s)
