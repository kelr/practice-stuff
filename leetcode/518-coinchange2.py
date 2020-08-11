
# Use bottom up DP to construct the amount of ways to make change with each denomination
# O(NC) where N is the amount and C is the number of coins
# O(N) space where N is the amount of coins
def change(amount, coins) -> int:
    # Only one way to make change for 0$
    if amount == 0:
        return 1

    ways = [0] * (amount+1)
    # Only one way to make change for 0$
    ways[0] = 1

    for denom in coins:
        for i in range(1, amount+1):
            # If this denomination can fit, add a way based on i - denom
            if denom <= i:
                ways[i] += ways[i - denom]


    return ways[amount]