class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        result = ''
        count = 1
        for i in range(0, len(s)):
            j = i + 1
            if j < len(s) and s[i] == s[j]:
                count += 1
            else:
                result += str(count)
                result += s[i]
                count = 1

        return result


sol = Solution()
print(sol.countAndSay(7))
