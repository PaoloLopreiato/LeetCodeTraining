#BF O(m^n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            
            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]
        
        return dfs(0, 0)
#O(m * n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
         # Initialize DP table
        dp = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        
        # Base case: There's one way to make the amount 0, which is to use no coins
        for i in range(len(coins) + 1):
            dp[0][i] = 1
        
        # Fill the DP table
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                # If we don't take the coin
                dp[a][i] = dp[a][i + 1]
                
                # If we take the coin, ensure we don't go out of bounds
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        
        return dp[amount][0]
    
#O(n)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        
        return dp[amount]