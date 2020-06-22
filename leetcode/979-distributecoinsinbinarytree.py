class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Go through the tree with DFS. For each node, figure out how many coins
# its children need or will give. Add these to the total number of moves.
# Then calculate the nodes new value from its children - 1 since it itself needs at least 1 coin.
# O(N) each node is visited once.
# O(N) worst case is when N == height of the tree.
def distributeCoins(root: TreeNode) -> int:
    moves = 0
    
    def dist(node):
        if not node:
            return 0
        
        # Get how many coins its children need or wants to give.
        left = dist(node.left)
        right = dist(node.right)
        
        # Add to the total number of moves regardless of give or take.
        moves += abs(left) + abs(right)
        
        # Calculate and return how many coins this node needs or wants to get rid of.
        return left + right + node.val - 1
    
    dist(root)
    return moves