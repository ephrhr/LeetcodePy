class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        tMap, window = {}, {}
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        have, need = 0, len(tMap)
        ans, ansLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in tMap and window[c] == tMap[c]:
                have += 1

            while have == need:
                if (r - l + 1) < ansLen:
                    ans = [l, r]
                    ansLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        return s[l: r + 1] if ansLen != float('inf') else ''


sol = Solution()
print(sol.minWindow('ADOBECODEBANC', 'ABC'))
print(sol.minWindow('aa', 'aa'))
