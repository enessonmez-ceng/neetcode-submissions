class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # (index , value)
        max_area = 0
        
        for i,h in enumerate(heights):
            if stack and stack[-1][1] <= h:
                stack.append((i,h))
            elif stack and stack[-1][1] > h:
                while stack and stack[-1][1] > h:
                    area = (i-stack[-1][0])*stack[-1][1] # width * height
                    popped = stack[-1][0]
                    stack.pop()
                    max_area = max(max_area,area)
                stack.append((popped,h))
            else:
                stack.append((i,h))
        
        n = len(heights)
        while stack:
            area = (n-stack[-1][0])*stack[-1][1]
            stack.pop()
            max_area = max(max_area,area)
        
        return max_area