"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
prices = [7,1,5,3,6,4]

def main():
    print(bt_buy_sell_1(prices))

#BAD TIME COMPLEXITY
def bt_buy_sell_0(prices):
    profit = 0
    for i in range(len(prices) - 1):
        for j in range(i+1, len(prices)):  
            profit = max((prices[j] - prices[i]),profit)
    return profit

#SLIDING WINDOW
def bt_buy_sell_1(prices):
    profit = 0
    min_price = float("inf")

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit

if __name__ == "__main__":
    main()