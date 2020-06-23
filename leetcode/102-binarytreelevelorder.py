class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 7:05
# Recursively obtain level order traversal with pre-order DFS. 
# For each node, add its children at the level in the output array if any children exist.
# Then DFS traverse through left and right children.
# O(N) time, visits each node once.
# O(N) space, output array has N integer values + N recursive calls in the worst case.
def levelOrderRec(root):
    def rec(node, level, out):
        if node:
            # Create a new level if needed
            if len(out) == level and (node.left or node.right):
                out.append([])
            
            if node.left:
                out[level].append(node.left.val)
            
            if node.right:
                out[level].append(node.right.val)
            
            rec(node.left, level + 1, out)
            rec(node.right, level + 1, out)

    if not root:
        return []

    out = [[root.val]]
    rec(root, 1, out)
    return out

# Cleaner for each recursive iteration to just add the current node.
def levelOrderRec2(root):
    def rec(node, level, out):
        if node:
            # Create a new level if needed
            if len(out) == level:
                out.append([])
            out[level].append(node.val)
            rec(node.left, level + 1, out)
            rec(node.right, level + 1, out)

    if not root:
        return []

    out = []
    rec(root, 0, out)
    return out

# 22m both
# Use BFS to add nodes to out in level order. Maintain a queue and pop from it as long as it is not empty.
# Add the nodes children to the queue and add the nodes current value to the output at the nodes level.
# O(N) time, each node is visited once.
# O(N) space, queue has N-1 elements in the worst case with 1 root and N-1 nodes + output array has N elements max.
def levelOrderIter1(root):
    queue = [[root, 0]]
    out = []
    while queue:
        node, level = queue.pop(0)
        if not node:
            continue

        if level == len(out):
            out.append([])

        if node.left:
            queue.append([node.left, level + 1])

        if node.right:
            queue.append([node.right, level + 1])

        out[level].append(node.val)

    return out

# Same as above but appends the current node's children to out instead of the current node.
def levelOrderIter2(root):
    if not root:
        return []

    queue = [[root, 0]]
    out = [[root.val]]
    while queue:
        node, level = queue.pop(0)
        level += 1

        children = [c for c in [node.left, node.right] if c]
        for child in children:
            if level == len(out):
                out.append([])

            queue.append([child, level])

            out[level].append(child.val)
    return out

# Compact
def levelOrderIter3(root):
    out = []
    # List of nodes at this current level
    level = [root]
    while root and level:
        # Add all the nodes at this level
        out.append([node.val for node in level])

        # Replace all the nodes in the level list with their children if they exist.
        level = [kid for node in level for kid in (node.left, node.right) if kid]
    return out