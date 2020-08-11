# Compute levenschtien distance with bottom up dp.
# O(N*M) time
# O(N*M) space, N*M elements in dp
def minDistance(self, word1: str, word2: str) -> int:
    # Create the dp matrix and initialize the first row for ascending edit distances
    dp = [[i for i in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
    
    # Initialize the first column
    for i in range(len(word2)+1):
        dp[i][0] = i
    
    for row in range(1, len(word2) + 1):
        for col in range(1, len(word1) + 1):
            if word2[row - 1] == word1[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                up = dp[row - 1][col]
                left = dp[row][col - 1]
                diag = dp[row - 1][col - 1]
                dp[row][col] = min(up, left, diag) + 1
    return dp[-1][-1]

# Compute levenschtien distance with top down DP
# O(N*M) time
# O(N*M) space, N*M elements in memo, min(N,M) on the recursion stack
def minDistance(self, word1: str, word2: str) -> int:
    memo = {}
    return dpHelper(word1, word2, 0, 0, memo)
        
def dpHelper(word1, word2, i, j, memo):
    # Base case for reaching the end of both words
    if i == len(word1) and j == len(word2):
        return 0
    
    # Reached the end of one word but not the other, just append the rest of the other one as inserts
    if i == len(word1):
        return len(word2) - j
    if j == len(word2):
        return len(word1) - i

    if (i, j) not in memo:
        if word1[i] == word2[j]:
            ans = dpHelper(word1, word2, i + 1, j + 1, memo)
        else: 
            insert = 1 + dpHelper(word1, word2, i, j + 1, memo)
            delete = 1 + dpHelper(word1, word2, i + 1, j, memo)
            replace = 1 + dpHelper(word1, word2, i + 1, j + 1, memo)
            ans = min(insert, delete, replace)
        memo[(i, j)] = ans
    return memo[(i, j)]