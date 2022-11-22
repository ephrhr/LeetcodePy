#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# @lc code=start


class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        possibleNums = []
        k = 1
        while k ** 2 <= n:
            possibleNums.append(k ** 2)
            k += 1
        count = 0
        q = {n}
        while q:
            count += 1
            nq = set()
            for i in q:
                for j in possibleNums:
                    if i == j:
                        return count
                    if i < j:
                        break
                    nq.add(i - j)
            q = nq
        return count
# @lc code=end
