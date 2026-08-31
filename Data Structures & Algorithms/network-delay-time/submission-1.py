class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [list() for i in range(n)]
        for u, v, t in times:
            adj[u - 1].append((v - 1, t))
        
        dist = [float('inf')] * n
        dist[k - 1] = 0
        h = [(0, k - 1)]
        while h:
            d, u = heapq.heappop(h)
            if dist[u] < d: continue
            dist[u] = d
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(h, (dist[v], v))
            
        ans = max(dist)
        return -1 if ans == float('inf') else ans