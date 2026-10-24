class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0

        while i<len(s):

            j = i

            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            j += 1

            decoded_strs.append(s[j : j + length])

            i = j + length
        
        return decoded_strs
                
        