class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Pre-order DFS through both trees at the same time.
# If t1 and t2 have a node, sum that value into t1.
# If t1 has a node and t2 doesnt, keep going
# If t2 has a node and t1 doesnt, create a new node with t2s value.
# Return t1
# O(N+K) where N is the number of nodes the trees share and K is the number of nodes they do not
# O(M) where M is the number of nodes in t1 but not t2.
def mergeTrees(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if not t1 and not t2:
        return None
    if t1 and t2:
        t1.val += t2.val
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
    elif t1:
        t1.left = mergeTrees(t1.left, t2)
        t1.right = mergeTrees(t1.right, t2)
    elif t2:
        t1 = TreeNode(t2.val)
        t1.left = mergeTrees(t1.left, t2.left)
        t1.right = mergeTrees(t1.right, t2.right)
    return t1

# More compact solution
def mergeTrees2(t1, t2):
    if not t1 and not t2:
        return None
    if not t1:
        return t2
    if not t2:
        return t1

    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)

    return t1