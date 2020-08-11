# Use bottom up DP to calculate the amount of coins needed to create an amount per denomination.
# O(NC) where N is the amount and C is the number of coins
# O(N) space
def coinChange(coins, amount) -> int:
    smallest = [float('inf')] * (amount+1)
    # 0 coins needed to make 0 dollars
    smallest[0] = 0

    for denom in coins:
        for i in range(1, amount+1):
            # If this denomination can fit in the current target amount
            if denom <= i:
                # Update the number of coins only if the denom interval + 1 before it was smaller
                smallest[i] = min(smallest[i], smallest[i - denom] + 1)

    minNumber = smallest[amount]
    return -1 if minNumber == float('inf') else minNumber