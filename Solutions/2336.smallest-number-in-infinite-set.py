#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#
import heapq
# @lc code=start
class SmallestInfiniteSet:

    def __init__(self):
        self.pq = [i for i in range(1, 1001)]
        self.st = set(self.pq)
        heapq.heapify(self.pq)

    def popSmallest(self) -> int:
        if self.pq:
            pop = heapq.heappop(self.pq)
            self.st.remove(pop)
            return pop

    def addBack(self, num: int) -> None:
        if num not in self.st:
            self.st.add(num)
            heapq.heappush(self.pq, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

