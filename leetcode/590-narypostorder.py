# Recursive DFS through the tree, append value after visiting children.
# O(N) time, visits and appends every node once.
# O(N) space, out list will have at most N elements.
def postorder(root):
    if not root:
        return []
    out = []
    for child in root.children:
        out += postorder(child)
    out.append(root.val)
    return out

# Use a stack to keep track of DFS history and the next child to iterate through.
# Prioritize the first child as long as it exists.
# If there are no more children, pop from the stack until some previous node
# has more children to iterate through.
# O(N) time, visits and appends every node once.
# O(N) space, stack and out list will have at most N elements each.
def postorderIter(root):
    stack = []
    out = []
    while root or stack:
        # Iterate and append the first child 
        while root:
            stack.append([root, 1])
            if not root.children:
                break
            root = root.children[0]

        root, idx = stack.pop()
        if idx < len(root.children):
            stack.append([root, idx + 1])
            root = root.children[idx]
        else:
            out.append(root.val)
            root = None

    return out

# Make a stack with the root. Pop from the stack, add to the output array
# then push the children onto the stack.
def postorderbetterIter(root):
    if root is None:
        return []

    stack, output = [root], []            
    while stack:
        root = stack.pop()
        output.append(root.val)
        for child in root.children:
            stack.append(child)

    return output[::-1]