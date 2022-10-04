class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mp = {}
        arr = [[] for i in range(len(nums) + 1)]

        for n in nums:
            mp[n] = mp.get(n, 0) + 1
        for key, val in mp.items():
            arr[val].append(key)

        result = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                result.append(n)
                if len(result) == k:
                    return result


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
