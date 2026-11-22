class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)  # key -> [value1,value2,...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        
        mylist = self.times[key]

        l = 0
        r = len(mylist) - 1
        old = ("","")
        while l <= r:
            mid = (l+r)//2
            tup = mylist[mid]
            if timestamp > tup[0]:
                old = tup
                l = mid + 1
            elif timestamp < tup[0]:
                r = mid - 1
            else:
                return tup[1]
        return old[1]