class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = dict()
        self.last = dict()
        self.q = deque()
        self.count = 0


    def get(self, key: int) -> int:
        if not key in self.d: return -1
        self.last[key] = self.count
        self.q.append((key, self.count))
        self.count += 1
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if not key in self.d and len(self.d) == self.cap:
            while self.q and (not self.q[0][0] in self.d or self.last[self.q[0][0]] != self.q[0][1]):
                self.q.popleft()
            del self.d[self.q[0][0]]
            del self.last[self.q[0][0]]
            self.q.popleft()
        self.last[key] = self.count
        self.d[key] = value
        self.q.append((key, self.count))
        self.count += 1
        
        
        
