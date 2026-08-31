class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        s = set()
        n = len(board)
        m = len(board[0])
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def check(i, j, idx, n, m, s):
            if not (0 <= i < n): return False
            if not (0 <= j < m): return False
            if (i, j) in s: return False
            if idx == len(word) - 1: return board[i][j] == word[idx]
            if board[i][j] != word[idx]: return False
            ret = False
            s.add((i, j))
            for dx, dy in delta:
                ret = ret or check(i + dx, j + dy, idx + 1, n, m, s)
            s.remove((i, j))
            return ret
        for i in range(n):
            for j in range(m):
                if check(i, j, 0, n, m, s): return True
        return False