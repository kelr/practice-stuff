class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# In-order DFS traverse through the tree, add sum if the value is between L and R.
# O(N) time, iterates through every node if L and R encompass the whole tree.
# O(N) space, worst case is every node except leaf has only 1 child creating N recursive calls on the stack.
# Can also be written as O(H) where H is the height of the BST.
def rangeSumBSTBrute(root, L: int, R: int) -> int:
    if not root:
        return 0
    currSum = 0
    if root.val > L:
        currSum += rangeSumBST(root.left, L, R)
    if L <= root.val and root.val <= R:
        currSum += root.val
    if root.val < R:
        currSum += rangeSumBST(root.right, L, R)
    return currSum

