class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive in order traversal of binary tree.
# O(N) time, visits each node once.
# O(N) space, creates an element in the output for each node.
def inorderTraversal(self, root)
    if not root:
        return None
    res = []
    left = self.inorderTraversal(root.left)
    if left:
        res += left
    res.append(root.val)
    right = self.inorderTraversal(root.right)
    if right:
        res += right
    return res

# Iterative traversal.
# O(N) time, visits each node once.
# O(N) space, at worst the stack could be N elements large + out is N elements.
def inorderTraversalIterative(self, root)
    stack = []
    out = []
    
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        out.append(root.val)
        root = root.right
    return out

# Test cases
# None root
# 1 element root
# large element root
# tree of only right children
# tree of only right children
# balanced tree
# bst, expected sorted output