# Since A goes first, they can either pick the 0th rock or the last rock. 
# Because the number of piles is even, the 0th rock is an even index and the last rock must be an odd index.
# If A picks the 0th rock, L can pick either the 1st rock or the last rock. These are both odd indexes.
# If A picks the last index rock, L can either pick the 0th rock or the 2nd to last rock. These are both even indexes.
# Whichever A picks, if A is consistent, L is forced to pick all even or all odd indexes.
# Since the sum of all piles is odd, there can be no ties, and A can just determine which of the
# even indexed or odd indexed piles have the greater number, and pick those, meaning A always wins.
# O(1), O(1)
def stoneGame(piles) -> bool:
    return True

# Use 2 dimensional DP to calculate all moves. One spot in the dp[i][j] represents the most amount of stones
# you can get more when picking in piles[i] to piles[j].
# If the top right element of the dp is positive, there is a guaranteed strat to win.
# This solution works with odd numbers of piles.
# O(N^2) time, generating N^2 / 2 solutions.
# O(N^2) space, generating N^2 / 2 solutions.
def stoneGame(piles):
    numPiles = len(piles)
    dp = [[0] * numPiles for i in range(numPiles)]

    for i in range(numPiles): 
        dp[i][i] = piles[i]

    for d in range(1, numPiles):
        for i in range(numPiles - d):
            front = piles[i] - dp[i + 1][i + d]
            rear = piles[i + d] - dp[i][i + d - 1]
            dp[i][i + d] = max(front, rear)

    return dp[0][-1] > 0