from heapq import heappush_max, heappop_max
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        removed = set()
        for i in range(k):
            heappush_max(h, (nums[i], i))
        ans = [h[0][0]]
        for i in range(k, len(nums)):
            heappush_max(h, (nums[i], i))
            removed.add((nums[i - k], i - k))
            while h[0] in removed:
                heappop_max(h)
            ans.append(h[0][0])
        return ans