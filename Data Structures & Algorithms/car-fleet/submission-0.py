class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        mylist = [(p,s) for p,s in zip(position,speed)]
        mylist.sort()
        n = len(mylist)
        res = 0
        stack = []
        
        for i in range(n-1,-1,-1):
            pos = mylist[i][0]
            speed = mylist[i][1]
            time = (target - pos)/speed

            if stack:
                if time > stack[-1][1]:
                    while stack:
                        stack.pop()
                    stack.append((pos,time))
                    res += 1
            else:
                stack.append((pos,time))

        if stack:
            while stack:
                stack.pop()
            res += 1
        return res    