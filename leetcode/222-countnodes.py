# Recursively check the left child and maintain a list of nodes for the previous level.
# Update the prevList with all the children of the next level if another level exists.
# If a level does not exist, total nodes is 2^level - 1 + len of the prevList.
# O(N) time, each node is added to the prevList once.
# O(N) space, each node is added to the prevList once + lgD recursive calls where D is depth of the tree.
def countNodes(root) -> int:
    if not root:
        return 0
    prev = [root]
    return rec(root, prev, 0)
        
def rec(node, prevList, level):
    if not node:
        level -= 1
        return (2**level) - 1 + len(prevList)
    tmp = []
    if not node.left and not node.right:
        tmp = prevList
    else:
        for n in prevList:
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)

    return rec(node.left, tmp, level + 1)


# Compare depths of the left and right subtrees.
# If they match, the left subtree is perfect and the right subtree is complete.
# If not, the left is complete and the right is perfect.
# O((lg^2 N), lgN + lg(N - 1) + lg(N - 2) + ... + lg(N-1)
# O(D) space, where D is depth of tree
def countNodes(root):
    if not root:
        return 0
    left = getDepth(root.left)
    right = getDepth(root.right)
    if left == right:
        return (2**left) + countNodes(root.right)
    else:
        return (2**right) + countNodes(root.left)

def getDepth(root):
    if not root:
        return 0
    return 1 + getDepth(root.left)


# Perform binary search on the tree to see if a node at idx exists.
# O(lg^2 N) time
# O(1) space
def countNodes(self, root: TreeNode) -> int:
    if not root:
        return 0
    
    # Get tree depth
    node = root
    depth = 0
    while node.left:
        node = node.left
        depth += 1

    if depth == 0:
        return 1
    
    # Label the imaginary leaf nodes at the bottom level from 0 to 2**depth - 1.
    # Perform binary search to check how many nodes exist.
    left = 0
    right = 2**depth - 1
    while left <= right:
        pivot = left + (right - left) // 2
        # If this node exists, then there are at least left number of nodes, shrink search space by half.
        if exists(pivot, depth, root):
            left = pivot + 1
        else:
            # If the node doesnt exist, shrink the search space by half.
            right = pivot - 1

    return (2**depth - 1) + left

# Traverse the tree using binary search with the imaginary leaf nodes at the bottom of the tree.
def exists(idx: int, d: int, root) -> bool:
    left = 0 
    right = 2**d - 1
    for _ in range(d):
        pivot = left + (right - left) // 2
        if idx <= pivot:
            root = root.left
            right = pivot
        else:
            root = root.right
            left = pivot + 1
    return root is not None