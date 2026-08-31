class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        visited = set()
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited: continue
                if grid[i][j] == 0: continue
                curr = 0
                s = [(i, j)]
                while s:
                    x, y = s.pop()
                    if grid[x][y] == 0: continue
                    if (x, y) in visited: continue
                    curr += 1
                    visited.add((x, y))
                    for dx, dy in delta:
                        if not 0 <= x + dx < len(grid): continue
                        if not 0 <= y + dy < len(grid[0]): continue
                        s.append((x + dx, y + dy))
                ans = max(ans, curr)
        return ans
