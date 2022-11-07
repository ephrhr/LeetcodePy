#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#
# @lc code=start


class Solution:
    def maximum69Number(self, num: int) -> int:
        tmp = num
        dig = 0
        maxSixDig = -1
        while tmp:
            if tmp % 10 == 6:
                maxSixDig = dig
            dig += 1
            tmp = tmp // 10
        return num + 3 * (10 ** maxSixDig) if maxSixDig != -1 else num

# @lc code=end

# string Solution
# class Solution:
#     def maximum69Number(self, num: int) -> int:
#         return int(str(num).replace('6', '9', 1))
