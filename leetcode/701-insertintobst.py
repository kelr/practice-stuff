class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Traverse BST looking for the position for the new val. Create and return the new node.
# Each node traversed through will update to the new node or reset its left or right child to the same node.
# O(N) time, when the tree is unbalanced so that each node has only one child except the leaf node.
# O(H) space, where H is the depth of the tree, since its one recursive call per depth.
def insertIntoBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    elif val > root.val:
        root.right = insertIntoBST(root.right, val)
    return root