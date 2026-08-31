class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        w = [1] * len(heights)

        s = []
        for i in range(len(heights)):
            if not s:
                s.append((heights[i], i))
                continue
            h, idx = s[-1]
            while heights[i] < h:
                s.pop()

                w[idx] += i - idx - 1

                if not s: break
                h, idx = s[-1]
            s.append((heights[i], i))
        
        while s:
            h, idx = s.pop()
            w[idx] += len(heights) - idx - 1

        for i in range(len(heights) - 1, -1, -1):
            if not s:
                s.append((heights[i], i))
                continue
            h, idx = s[-1]
            while heights[i] < h:
                s.pop()

                w[idx] += idx - i - 1

                if not s: break
                h, idx = s[-1]
            s.append((heights[i], i))
        
        while s:
            h, idx = s.pop()
            w[idx] += idx

        print(w)

        return max([heights[i] * w[i] for i in range(len(heights))])
        