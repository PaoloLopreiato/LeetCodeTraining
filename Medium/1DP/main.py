#Brute Force 
def bruteforce(n):
    if n <= 1:
        return n
    return bruteforce(n - 1) + bruteforce(n - 2)
print(bruteforce(5))

#Memorization
def memorization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    
    cache[n] = memorization(n - 1) + memorization(n - 2)
    return cache[n]
print(memorization(5, {}))

#Dynamic Programming
def dp(n):
    if n < 2:
        return n
    
    dp[0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]
print(dp(5))
