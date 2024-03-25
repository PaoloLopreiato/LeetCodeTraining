"""
70. Climbing Stairs
Easy
Topics
Companies
Hint
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
n = 5

def main():
    #print(climbStairs(n))
    print(climb_stairs_0(n))


"""
Base Cases: We handle the base cases where n is 1 or 2. When there's only one step, there's only one way to climb it (1). When there are two steps, there are two ways to climb (1 + 1 or 2 steps at once).

Dynamic Programming Approach: For n >= 3, we initialize two variables prev and curr to represent the number of ways to reach the previous step and the current step, respectively. We start iterating from the third step (i = 3) up to n.

Updating Values: At each step i, the number of ways to reach the i-th step (curr) is the sum of the number of ways to reach the previous step (prev) and the number of ways to reach the step before the previous step (curr). This is because from the previous step, we can either take one step to reach the current step (prev), or we can take two steps to directly reach the current step (curr). So, next_step = prev + curr.

Updating Variables: After calculating next_step, we update prev to be the value of curr, and curr to be the value of next_step, preparing for the next iteration.

Returning Result: After iterating through all steps from 3 to n, curr holds the number of ways to reach the n-th step. So, we return curr.
"""
def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    prev = 1
    curr = 2  

    for i in range(3, n + 1):
        next_step = prev + curr
        prev = curr
        curr = next_step
    
    return curr

def climb_stairs_0(n):
    one, two = 1, 1
    for i in range(n-1):
        tmp = one
        one = one + two
        two = tmp
    return one


if __name__ == "__main__":
    main()