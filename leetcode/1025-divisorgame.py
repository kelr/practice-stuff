
# If N is even, its possible to win
# If N is odd, we lose.

# If N starts as even, A can always remove 1 to turn it odd.
# If N starts as odd, and is 1 we instalose. If it is > 1, odd numbers only have odd factors
# so A is forced to make N even for B. If B never turns it even for A, B is guaranteed to win.
# O(1), O(1)
def divisorGame(N: int) -> bool:
    return N % 2 == 0