
# Recursive DFS through the tree.
# O(N) time, visits and appends every node once.
# O(N) space, out list will have at most N elements.
def preorder(root):
    if not root:
        return []
    out = []
    out.append(root.val)
    for child in root.children:
        out += preorder(child)
    return out

# Use a stack to keep track of DFS history and the next child to iterate through.
# Prioritize the first child as long as it exists.
# If there are no more children, pop from the stack until some previous node
# has more children to iterate through.
# O(N) time, visits and appends every node once.
# O(N) space, stack and out list will have at most N elements each.
def preorderIterative(root):
    stack = []
    out = []
    while root or stack:
        # Iterate and append the first child 
        while root:
            stack.append([root, 1])
            out.append(root.val)
            if not root.children:
                break
            root = root.children[0]
        
        root, idx = stack.pop()
        if idx < len(root.children):
            stack.append([root, idx + 1])
            root = root.children[idx]
        else:
            root = None

    return out

# Make a stack with the root. Pop from the stack, add to the output array
# then push the children onto the stack in reverse.
def preorderBetterIter(root):
    if root is None:
        return []
    
    stack, output = [root], []            
    while stack:
        root = stack.pop()
        output.append(root.val)
        for child in root.children[::-1]:
            stack.append(child)
            
    return output