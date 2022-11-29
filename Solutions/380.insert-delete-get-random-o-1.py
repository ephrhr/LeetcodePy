#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#
import random
# @lc code=start


class RandomizedSet:

    def __init__(self):
        self.data = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.data.append(val)
        self.mp[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        lastElement = self.data[-1]
        targetIndex = self.mp[val]
        self.mp[lastElement] = targetIndex
        self.mp.pop(val)
        self.data[targetIndex] = lastElement
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
