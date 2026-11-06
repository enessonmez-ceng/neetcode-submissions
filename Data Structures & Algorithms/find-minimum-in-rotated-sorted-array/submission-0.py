class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        if nums[l] < nums[r]:
            return nums[0]

        while l < r and r-l > 1: 
            mid = (l + (r-l)//2)

            if nums[mid] > nums[l]:
                l = mid
            elif nums[mid] < nums[l]:
                r = mid
            
        return nums[r]