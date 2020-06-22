class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Return a nodes value concatenated with each of its children nodes if it is lonely.
# The parent tells the child if its lonely or not.
# O(N) time, visits each node once.
# O(N) space, N recursion depth at max for a tree with only 1 childrens except leaf. + N-1 output array elements.
def getLonelyNodes(root: TreeNode):
        return rec(root, False)
        
def rec(node: TreeNode, isLonely: bool):
    out = [node.val] if isLonely else []
    if not node.left and not node.right:
        return out
    elif not node.left and node.right:
        return out + rec(node.right, True)
    elif node.left and not node.right:
        return out + rec(node.left, True)
    else:
        return out + rec(node.left, False) + rec(node.right, False)


# Parent appends children to output array if it sees that it is lonely.
# DFS through nodes that exist.
def getLonelyNodes(root: TreeNode):
    lonely = []
    rec(root, lonely)
    return lonely

def rec(node: TreeNode, lonely):
    if not node.left and node.right:
        lonely.append(node.right.val)
    if node.left and not node.right:
        lonely.append(node.left.val)
    
    if node.left:
        rec(node.left, lonely)
    if node.right:
        rec(node.right, lonely)
