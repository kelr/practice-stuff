 # Compare each price with itself and each subsequent price to find the max
 # O(N^2) time, since there are N(N+1)/2 comparisons
 # O(1) space
 def maxProfitBrute(self, prices) -> int:
    if not prices:
        return 0
    profitMax = 0
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            profit = prices[j] - price
            if profit > profitMax:
                profitMax = profit
    return profitMax

# Loop through prices and find the curr min. If the current val and the curr min
# yield a greater max profit, save that max profit.
# O(N), single pass
# O(1) space
def maxProfit(self, prices) -> int:
    if not prices:
        return 0
    currMin = float("inf")
    maxProfit = 0
    for price in prices:
        if price < currMin:
            currMin = price
        elif price - currMin > maxProfit:
            maxProfit = price - currMin
    return maxProfit