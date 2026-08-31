class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            h = set()
            v = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in h: return False
                    h.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in v: return False
                    v.add(board[j][i])
        
        for i in range(9):
            s = set()
            x = i % 3 * 3
            y = i // 3 * 3
            for dx in range(3):
                for dy in range(3):
                    if board[x + dx][y + dy] == ".": continue
                    if board[x + dx][y + dy] in s: return False
                    s.add(board[x + dx][y + dy])
        
        return True