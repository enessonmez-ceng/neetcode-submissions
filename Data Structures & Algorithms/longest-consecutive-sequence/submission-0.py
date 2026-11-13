class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set()

        for n in nums:
            seen.add(n)

        max_length = 0

        for s in seen:
            if s - 1 not in seen:
                length = 1
                i = 1
                while s + i in seen:
                    length += 1
                    i += 1
                max_length = max(max_length,length)
        return max_length