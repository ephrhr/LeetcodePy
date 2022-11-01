import collections


class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map[key]
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            elif arr[mid][0] > timestamp:
                r = mid
        return "" if r == 0 else arr[r - 1][1]
