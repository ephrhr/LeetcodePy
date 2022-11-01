class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        result = ''
        values = list(symbol.keys())
        for v in values:
            while num >= v:
                num -= v
                result += symbol[v]

        return result


sol = Solution()
print(sol.intToRoman(1994))
