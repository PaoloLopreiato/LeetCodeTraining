#Input: heights = [2,1,5,6,2,3]
#Output: 10
heights = [9,0,6,7]

def main():
    print(Largest_rectangle_in_histogram(heights))


#Must redo 
def Largest_rectangle_in_histogram(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))
        
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    
    return max_area
    
if __name__ == "__main__":
    main()