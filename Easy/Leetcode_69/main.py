"""
69. Sqrt(x)
Easy
Topics
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""
import math

x = 4

def main():
    #print(sqrt_chearing(x))
    print(sqrt_legit_0(x))
    print(sqrt_legit_1(x))

#My Solution(IT WORKS)
def sqrt_legit_0(x):
    divisor = 1
    guess = x / divisor
    while guess * guess > x:
        divisor += 1
        guess = x / divisor
    if guess * guess == x:
        return int(guess)
    else:
        return int(math.floor(guess))

#Solution 2(GPT)
def sqrt_legit_1(x):
    divisor = 1
    while divisor * divisor <= x:
        divisor += 1
    return int(divisor - 1)


#cheating
def sqrt_chearing(x):
    return math.floor(math.sqrt(8))
   
if __name__ == "__main__":
    main()