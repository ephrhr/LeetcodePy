#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List
from collections import defaultdict
# @lc code=start


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # handle odd large edge cases
        charFreq = defaultdict(int)
        for c in word:
            charFreq[c] += 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                charFreq[board[i][j]] -= 1

        for f in charFreq.values():
            if f > 0:
                return False

        # backtracking

        def dfs(r, c, i):
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or i >= len(word) or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            tmp = board[r][c]
            board[r][c] = '#'
            ans = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i +
                                              1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            board[r][c] = tmp
            return ans

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
# @lc code=end
# create queue to store start characters in the grid.
# dequeue and search. return true if find the word else false.
