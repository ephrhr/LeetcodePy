class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)
        preProd, postProd = 1, 1
        for l in range(len(nums)):
            r = len(nums) - 1 - l
            ans[l] *= preProd
            preProd *= nums[l]
            ans[r] *= postProd
            postProd *= nums[r]
        return ans


sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
