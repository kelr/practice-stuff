class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterate through the preorder list and insert each value into the BST.
# O(N^2) time, N iterations to traverse preorder, worst case N iterations to insert into BST.
# O(H) space, where H is the height of the BST
def bstFromPreorder(preorder) -> TreeNode:
    root = None
    for val in preorder:
        if not root:
            root = TreeNode(val)
        else:
            insert(root, val)
    return root
    
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Use a stack to keep track of the order of created nodes.
# If a new node is less than the head, set the new node as the left child of the head.
# If the new node is greater than the head, keep popping off values off the stack
# Until the stack is empty or until you find a value greater than the new node.
# Set the new node as the right child of the most recently popped node.
# Push onto the stack every iteration.
# O(N) time, each node is pushed onto the stack once and the stack is popped at most N-1 times
# (every child is a left node except the last one which is the right child of the root)
# O(N) space, stack can grow up to N elements (each node only has a left child except the leaf)
def bstFromPreorder(preorder) -> TreeNode:
    prev = 0
    # Preorder is guaranteed to have at least 1 element
    root = TreeNode(preorder[0])
    stack = [root]
    
    for val in preorder[1:]:
        newNode = TreeNode(val)
        if val < stack[-1].val:
            stack[-1].left = newNode
        else:
            while stack and val > stack[-1].val:
                prev = stack.pop()
            prev.right = newNode
        stack.append(newNode)
    return root
