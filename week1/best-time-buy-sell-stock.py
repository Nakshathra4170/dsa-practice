"""
LeetCode 121: Best Time to Buy and Sell Stock
Problem: Find max profit from buying and selling once
Approach: Single pass, track min price seen so far
Time: O(n) | Space: O(1)
"""

def maxProfit(prices):
    
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        potential_profit = price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, price)
    
    return max_profit

if __name__ == "__main__":
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Test 1: {prices1}")
    print(f"Output: {maxProfit(prices1)}")  # Expected: 5
    print()
    
    prices2 = [7, 6, 4, 3, 1]
    print(f"Test 2: {prices2}")
    print(f"Output: {maxProfit(prices2)}")  # Expected: 0