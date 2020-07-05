# Initialize memo with F(0) = 0, F(1) = 1
memo = {
    0: 0,
    1: 1,
}
# Top down DP
# If F(N) has been computed before, just return what memo stored.
# If not, calculate F(N) and store it in the memo.
# O(N) time, each value of N from 2 to N is computed and stored once.
# O(N) space, up to N values in memo.
def fib(N: int) -> int:
    if N in memo:
        return memo[N]
    memo[N] = fib(N-1) + fib(N-2)
    return memo[N]

# Bottom up DP
# From 2 to N, build the next value in memo with the previous two.
# The value of F(N) is memo[N-1] + memo[N-2]
# O(N) time, N-2 iterations to build memo.
# O(N) space, memo has N elements in total.
def fib(N: int) -> int:
    if N == 0 or N == 1:
        return memo[N]
    
    for num in range(2, N):
        memo[num] = memo[num-1] + memo[num-2]
        
    return memo[N-1] + memo[N-2]

# Same bottom up DP using constant space.
# prev1 represents N-2 and prev2 represents N-1.
# Calculate the current fib number with prev1 + prev2
# Then adjust each value up by one.
# O(N) time, O(1) space
def fib(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    prev1 = 0
    prev2 = 1
    for _ in range(2, N):
        res = prev1 + prev2
        prev1 = prev2
        prev2 = res
        
    return prev1 + prev2

# Calculate the Nth fib with the golden ratio.
# Constant space, but time depends on how exponentiation is implemented.
# Also, loses precision when N is large.
def fib(N):
    golden_ratio = (1 + 5 ** 0.5) / 2
    return int((golden_ratio ** N + 1) / 5 ** 0.5)