def bruteforce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
    return (bruteforce(r + 1, c, rows, cols),
            bruteforce(r, c + 1, rows, cols))
print(bruteforce(0,0,4,4))

def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c]  > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1
    
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache),
                   memoization(r, c + 1, rows, cols, cache))   
    return cache[r][c]
print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))