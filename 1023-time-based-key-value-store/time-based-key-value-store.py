class TimeMap:

    def __init__(self):
        self.kv = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.kv[key]
        left = 0
        right = len(values)-1

        while left <= right:
            mid = (left+right)//2
            cur_val, cur_timestamp =  values[mid]
            if cur_timestamp <= timestamp:
                res = cur_val
                left = mid +1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)