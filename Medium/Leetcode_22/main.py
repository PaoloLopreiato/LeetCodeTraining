"""
22. Generate Parentheses
Medium
Topics
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]
n = 3

def main():
    print(parenthesis_generator(n))

def parenthesis_generator(n):
    stack = []
    result = []
    
    def backtrack(o,c):
        if o == c == n:
            result.append("".join(stack))
            return
        if o < n:
            stack.append("(")    
            backtrack(o + 1,c)
            stack.pop()
        if c < o:
            stack.append(")")    
            backtrack(o,c + 1)
            stack.pop()    
    backtrack(0, 0)
    return result
    
if __name__ == "__main__":
    main()