from collections import defaultdict
from bisect import bisect_left
class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_left(self.d[key], (timestamp, ))
        print(self.d[key], timestamp)
        if not self.d[key]: return ""
        if idx == len(self.d[key]):
            return self.d[key][-1][1]
        if self.d[key][idx][0] > timestamp:
            idx -= 1
        if idx < 0: return ""
        return self.d[key][idx][1]
