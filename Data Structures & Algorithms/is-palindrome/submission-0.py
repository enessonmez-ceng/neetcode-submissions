class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(w for w in s if w.isalnum())
        clean = clean.lower()
        n = len(clean)

        left = 0
        right = n-1

        while left<right:
            if clean[left] != clean[right]:
                return False
            
            left += 1
            right -= 1
        return True