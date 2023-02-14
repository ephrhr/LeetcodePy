#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        a = list(a)
        b = list(b)
        carry = 0
        while a or b or carry == 1:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            ans += str(carry % 2)
            carry //= 2
        return ans[::-1]
# @lc code=end
# Using libs
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, 2) + int(b, 2))[2:]

