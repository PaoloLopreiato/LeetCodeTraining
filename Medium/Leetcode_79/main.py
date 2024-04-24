class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        seen = set()
        
        def dfs(row, col, i):
            if i == len(word):
                return True
            #Out of bound, Char not in Board, Duplicate Char
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or word[i] != board[row][col] or (row, col) in seen: 
                return False
            
            seen.add((row, col))
            
            res = dfs(row + 1, col, i + 1) or dfs(row - 1, col, i + 1) or dfs(row, col + 1, i + 1) or dfs(row, col - 1, i + 1)
            seen.remove((row, col))
            return res
        
        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True
        
        return False