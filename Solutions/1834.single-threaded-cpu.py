#
# @lc app=leetcode id=1834 lang=python3
#
# [1834] Single-Threaded CPU
#
from typing import List
from heapq import heapify, heappop, heappush
# @lc code=start


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        ans = []
        pq = []
        time = tasks[0][0]
        while len(ans) < n:
            while (i < n) and (tasks[i][0] <= time):
                heappush(pq, (tasks[i][1], tasks[i][2]))
                i += 1
            if pq:
                timeDiff, index = heappop(pq)
                time += timeDiff
                ans.append(index)
            elif i < n:
                time = tasks[i][0]
        return ans

# @lc code=end
