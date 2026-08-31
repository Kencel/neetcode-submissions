from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.buffer = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.buffer) < self.k:
            heappush(self.buffer, val)
        else:
            heappush(self.buffer, val)
            heappop(self.buffer)
        return self.buffer[0]
