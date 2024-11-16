class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []

        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
            
        values = self.timemap[key]
        result = ""

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            val, time = values[mid]

            if time <= timestamp:
                result = val
                left = mid + 1

            else:
                right = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)