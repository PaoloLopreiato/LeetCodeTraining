"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

x = -121

def main():
    print(palindrome_cheker(x))

def palindrome_cheker(x):
    x = str(x)
    return x == x[::-1]
    #y = x[::-1]
    #if x == y:
        #return True
    #else:
        #return False


if __name__ == "__main__":
    main()