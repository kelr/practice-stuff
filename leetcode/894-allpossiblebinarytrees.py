# Cache stores previously computed trees of N nodes, so we dont have to recompute them.
cache = {
    1: [TreeNode(0)]
}

# Iterate through every possible FBST and create a root node for each.
# Save built FBSTs of size N in a cache to speed up calculations.
# This solution will tie nodes together, so a proper solution should do a deep copy of 
# each cached FBST instead.
# O(2^N) time and space since the number of FBSTs for N number of nodes is the N-1/2th Catalan number 
# if N is even.
def allPossibleFBT(self, N: int) -> List[TreeNode]:
    if N in self.cache: 
        return self.cache[N]

    ret = []
    # Skip over even numbers since there cannot be a full BST with an even number of nodes.
    for i in range(1, N - 1, 2):
        # Get a list of all the root nodes of size i
        for left in self.allPossibleFBT(i):
            # Get a list of all the root nodes of size N - i - 1
            for right in self.allPossibleFBT(N - i - 1):
                # Create a new root node for each possible full BST
                root = TreeNode(0)
                root.left = left
                root.right = right
                ret.append([root])
    self.cache[N] = ret
    return ret