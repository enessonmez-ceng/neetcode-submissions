class Solution:

    def encode(self, strs: List[str]) -> str:
        encod = ""
        for s in strs:
            encod += str(len(s)) + "#" + s
        return encod
    def decode(self, s: str) -> List[str]:
        decoded = []
        n = len(s)
        i = 0
        while i<n:
            j = s.find("#", i)
            length = int(s[i:j])
            decoded.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded