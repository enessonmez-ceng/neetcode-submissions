class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # prefix&suffix - optimal
        n = len(nums)
        res = [1]*n
        res[0] = 1
        res[n-1] = 1
        for i in range(1,n):
            res[i] = res[i-1]*nums[i-1]
        postfix = 1
        for i in range(n-2,-1,-1):
            postfix *= nums[i+1]
            res[i] *= postfix
        return res