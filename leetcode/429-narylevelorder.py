
# Perform BFS over the tree, keep a level indicator on the queue.
# When adding to the output array, just extend it at the current level.
# O(N) time, visits all nodes once.
# O(N) space, queue is at most N elements of [node, level] + out with N ints.
def levelOrder(root):
    if not root:
        return []

    queue = [[root, 0]]
    out = [[root.val]]

    while queue:
        root, level = queue.pop(0)
        if root.children:
            # Add a level if needed
            if level + 1 >= len(out):
                out.append([])

            # Append to the output array for this level.
            out[level + 1].extend([child.val for child in root.children])

            # Add this node's children to the queue for the next level.
            queue.extend([[child, level+1] for child in root.children])
    return out


# Recursive version.
def levelOrderRecursive(root):
    if not root:
        return []
    out = []
    res(root, 0, out)
    return out
    
def res(node, level, out):
    # Add a new level to the output if it doesn't exist
    if len(out) == level:
        out.append([])
    
    out[level].append(node.val)
    
    for child in node.children:
        res(child, level + 1, out)