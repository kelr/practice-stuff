
# Loop through each position in the output array and manually calculate the block sum.
# O(N*M*K^2) time. M*N to iterate through the output matrix. Each block sum calculation takes (K+2)^2 time.
# O(N*M) space, output matrix.
def matrixBlockSum(mat, K: int):
    m = len(mat)
    n = len(mat[0])
    
    out = [[0] * n for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            low_i = 0 if i-K < 0 else i-K
            high_i = m-1 if i+K > m-1 else i+K
            low_j = 0 if j-K < 0 else j-K
            high_j = n-1 if j+K > n-1 else j+K
            
            s = 0
            for inner_i in range(low_i, high_i+1):
                for inner_j in range(low_j, high_j+1):
                    s += mat[inner_i][inner_j]
            out[i][j] = s
    return out
        
# Use a Summed Area Table https://computersciencesource.wordpress.com/2010/09/03/computer-vision-the-integral-image/
# O(N*M) time, N*M to iterate through the output matrix. Calculating the sum is constant time.
# O(N*M) space, total space used is N*M for the output matrix and another N*M for the Summed Area Table.
def matrixBlockSumDP(mat, K: int):
    m = len(mat)
    n = len(mat[0])

    sumAreaTable = [[0] * (n + 1) for _ in range(m + 1)]
    # Build the SAT. Each new position is calculated as its left SAT value + its top SAT value - its top left SAT value + the actual value.
    for i in range(m):
        for j in range(n):
            sumAreaTable[i + 1][j + 1] = sumAreaTable[i + 1][j] + sumAreaTable[i][j + 1] - sumAreaTable[i][j] + mat[i][j]

    out = [[0] * n for _ in range(m)]        

    # Cut out rectangles to find the area with the SAT.
    for i in range(m):
        for j in range(n):
            # Range limit the values if they exceed matrix boundaries
            r1 = max(0, i - K)
            r2 = min(m, i + K + 1)

            c1 = max(0, j - K)
            c2 = min(n, j + K + 1)

            # +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
            # |               |   |         |    |   |   |           |   |         |    |   |   |          |
            # |   (r1,c1)     |   |         |    |   |   |           |   |         |    |   |   |          |
            # |   +------+    |   |         |    |   |   |           |   +---------+    |   +---+          |
            # |   |      |    | = |         |    | - |   |           | - |      (r1,c2) | + |   (r1,c1)    |
            # |   |      |    |   |         |    |   |   |           |   |              |   |              |
            # |   +------+    |   +---------+    |   +---+           |   |              |   |              |
            # |        (r2,c2)|   |       (r2,c2)|   |   (r2,c1)     |   |              |   |              |
            # +---------------+   +--------------+   +---------------+   +--------------+   +--------------+
            out[i][j] = sumAreaTable[r2][c2] - sumAreaTable[r2][c1] - sumAreaTable[r1][c2] + sumAreaTable[r1][c1]

    return out