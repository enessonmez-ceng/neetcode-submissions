class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hashmap = defaultdict(list) # val -> index list

        for i,n in enumerate(numbers):
            hashmap[n].append(i+1)
        
        for i,n in enumerate(numbers):
            diff = target - n
            if diff in hashmap:
                if len(hashmap[n]) > 1:
                    return [hashmap[n][0],hashmap[diff][1]]
                return [hashmap[n][0],hashmap[diff][0]]
            
        return []