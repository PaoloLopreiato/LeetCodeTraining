"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] 
target = 3
#Output: true

def main():
    print(search_2d_matrix_1(matrix, target))

#MEH
def search_2d_matrix_0(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // cols][mid % cols]
        
        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False    

#YESSIR
def search_2d_matrix_1(matrix, target):
    row, col = len(matrix), len(matrix[0])
    
    top, bot = 0, row - 1
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1 
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    
    if not top <= bot:
        return False
           
    left, right = 0, col - 1 
    while left <= right:
        mid = (left + right) // 2
        
        if matrix[row][mid] == target:
            return True
        
        if target < matrix[row][mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False
    
if __name__ == "__main__":
    main()