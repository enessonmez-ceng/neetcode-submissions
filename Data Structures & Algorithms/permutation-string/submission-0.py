class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        k = len(s1)
        for s in s1:
            freq[s] += 1
        
        l , r = 0 , 0

        temp = defaultdict(int)

        while r < len(s2) :
            temp[s2[r]] += 1
            r += 1

            if r-l > k:
                temp[s2[l]] -= 1
                if temp[s2[l]] <= 0:
                    del temp[s2[l]]
                l += 1
            
            if temp == freq:
                return True
            
        return False