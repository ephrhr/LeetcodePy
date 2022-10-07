import collections

#TC: O(nlogn)


class MyCalendarThree:

    def __init__(self):
        self.timemap = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timemap[start] += 1
        self.timemap[end] -= 1
        maxCount = 0
        count = 0
        times = list(self.timemap.keys())
        times.sort()
        for time in times:
            count += self.timemap[time]
            maxCount = max(maxCount, count)
        return maxCount


#TC: O(logn)
# Segement Tree with Lazy Propagation


# class MyCalendarThree(object):

#     def __init__(self):
#         self.seg = collections.defaultdict(int)
#         self.lazy = collections.defaultdict(int)

#     def book(self, start, end):
#         def update(s, e, l=0, r=10**9, ID=1):
#             if e <= l or r <= s:
#                 return
#             if s <= l < r <= e:
#                 self.seg[ID] += 1
#                 self.lazy[ID] += 1
#             else:
#                 m = (l + r) // 2
#                 update(s, e, l, m, 2 * ID)
#                 update(s, e, m, r, 2 * ID + 1)
#                 self.seg[ID] = self.lazy[ID] + max(self.seg[2 * ID], self.seg[2 * ID + 1])
#         update(start, end)
#         return self.seg[1]
