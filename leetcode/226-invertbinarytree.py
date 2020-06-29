class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# If a node exists and has children, swap the children then pre-order DFS.
# O(N) time, checks every node once
# O(N) space, N calls on the stack if each node has one child except the leaf.
def invertTree(root):
    if not root:
        return
    if root.left or root.right:
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        invertTree(root.left)
        invertTree(root.right)
    return root 


# Iterative version. Use a queue, swap if there are any children.
# Then push the not-none children into the queue.
# O(N) time, checks every node
# O(N) space, queue can grow up to all the elements in one level of the tree.
def invertTreeIter(root):
    if not root:
            return None
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            if node.left or node.right:
                tmp = node.left
                node.left = node.right
                node.right = tmp
                queue.extend([n for n in [node.left, node.right] if n is not None])

        return root