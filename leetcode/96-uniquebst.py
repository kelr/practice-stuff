import math

# The total number of unique structures for a BST with N nodes is the sum of all
# unique BSTs created with each node as the root. 
# For example if N = 3, with a BST that has nodes of values 1, 2 and 3
# the total number of nodes is the sum of unique BSTS created with a root at 1 (2), root at 2 (1), and root at 3 (2).
# for a total of 5.
# This alg iterates over each node and recursively breaks down each BST created with the node as the root
# with a left subtree and a right subtree.
# Ex:
# For N = 3 and values of [1,2,3], root 1 has 0 nodes on the left and 2 nodes on the right
# root 2 has 1 node on the left and one node on the right
# root 3 has 2 nodes on the left and 1 node on the right.
# O(N^2) using memoization. 
# O(N) space, memo will have N+1 elements.
memo = {
    0 : 1, 
    1 : 1
}
def numTrees(n: int) -> int:
    val = 0
    if n in memo:
        val += memo[n]
    else:
        for i in range(n):
            val += numTrees(i) + numTrees(n - i - 1)
        memo[n] = val
    return val

# Num of unique BSTs for n is just the nth Catalan Number so just do that in O(1) time and space.
def numTreesCatalan(n: int) -> int:
    return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))

print(numTrees(50))