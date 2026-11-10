class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def findmost(ht : dict):
            most = 0
            char = ''
            for key,value in ht.items():
                if value > most:
                    most = value
                    char = key
            return (most,char)
        
        l = 0
        ht = defaultdict(int)
        most = 0
        char = ""
        res = 0
        for r in range(len(s)):
            ht[s[r]] += 1
            
            ret = findmost(ht)
            most , char = ret[0] , ret[1]

            while (r - l + 1) - most > k:
                ht[s[l]] -= 1
                l += 1
                ret = findmost(ht)
                most , char = ret[0] , ret[1]
            res = max(res,r-l+1)
        return res
            
            