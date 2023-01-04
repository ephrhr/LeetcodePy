#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#
from typing import List
from collections import Counter
# @lc code=start


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks).values()
        ans = 0
        for v in count:
            if v == 1:
                return -1
            else:
                ans += (v + 2) // 3

        return ans
# @lc code=end
