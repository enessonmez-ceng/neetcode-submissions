class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        L = [0]*n
        maxl = 0
        for i in range(1,n):
            maxl = max(maxl,height[i-1])
            L[i] = maxl

        R = [0]*n
        maxr = 0
        for i in range(n-2,-1,-1):
            maxr = max(maxr,height[i+1])
            R[i] = maxr

        res = 0
        for i in range(n):
            calc = min(L[i],R[i]) - height[i]

            if calc > 0:
                res += calc
        return res