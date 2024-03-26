import collections

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def main():
    #print(sudoku_cheker_0(board))
    print(sudoku_cheker_1(board))
    
def sudoku_cheker_0(board):
    for row in board:
        if not is_valid(row):
            return False
    
    for column in zip(*board):
        if not is_valid(column):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = []
            for x in range(i, i + 3):  
                for y in range(j, j + 3): 
                    sub_box.append(board[x][y]) #building an array starting from board
            if not is_valid(sub_box):
                return False
            
    return True
      

def is_valid(nums):
    seen = set()
    for num in nums:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True
 
#Solution 2
def sudoku_cheker_1(board):
    columns = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) #r/3 c/3
    
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in squares[(r//3, c//3)]):
                return False
            else:
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
    return True

if __name__ == "__main__":
    main()