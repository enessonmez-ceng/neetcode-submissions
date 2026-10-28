class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # we use monotonic stack
        stack = []
        n = len(temperatures)
        res = [0]*n
        for i in range(n):
            t = temperatures[i]

            while stack and t > temperatures[stack[-1]]:
                popped = stack.pop()
                res[popped] = i - popped
                
            stack.append(i)

        while stack:
            stack.pop()
        return res