#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List
# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]

        def isValid(r, c):
            for i in range(n):
                if board[i][c] == 'Q':
                    return False
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            return True

        def backtrack(r):
            if r == n:
                ans.append([''.join(s) for s in board])
                return

            for c in range(n):
                if not isValid(r, c):
                    continue
                board[r][c] = 'Q'
                backtrack(r + 1)
                board[r][c] = '.'

        backtrack(0)
        return ans
# @lc code=end
