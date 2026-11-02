class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            h = min(height[l],height[r])
            area = abs(r-l)*h
            max_area = max(max_area,area)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area