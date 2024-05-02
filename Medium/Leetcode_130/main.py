board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "F"
            
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or c == 0 or r == ROWS - 1 or c == COLS - 1) and board[r][c] == "O":
                    dfs(r, c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "F":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
