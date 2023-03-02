#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        while i < len(chars):
            count = 1
            while i + count < len(chars) and chars[i + count] == chars[i]:
                count += 1
            if count > 1:
                sub = list(str(count))
                chars[i + 1:i + count] = sub
                i += len(sub) + 1
            else:
                i += 1
        return len(chars)
# @lc code=end

