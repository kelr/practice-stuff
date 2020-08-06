# Find the closest value in the tree to target
def closestValue(root, target) -> int:
    return binarySearchInBst(root, target, root.val)

# Maintain the current closest value per recursive call.
# If the value itself is found, return that. If a new closer value is found,
# update the closest value and continue searching.
# Given that the tree is a BST, we can binary search on it making average search times faster.
# O(N) time, on average its O(lgN) but worst case will be N if the tree is just a linked list.
# O(N) space, on average its O(lgN), up to N recursive calls on the call stack.
def binarySearchInBst(node, target, closest) -> int:
    if not node:
        return closest
    
    # Can't get closer than the value itself
    if target == node.val:
        return node.val
    
    # Found a new closer value
    if abs(target - closest) > abs(target - node.val):
        closest = node.val

    # Traverse only in one direction due to BST property.
    if target < node.val:
        return binarySearchInBst(node.left, target, closest)
    return binarySearchInBst(node.right, target, closest)

# Regular DFS implementation. Searches both children of the tree if the BST property does not hold.
# O(N) time, searches every node
# O(N) space, worst case for a linked list tree where there will be N recursive calls on the stack.
def dfs(node, target, closest) -> int:
    if not node:
        return closest
    
    # Can't get closer than the value itself
    if node.value == target:
        return node.value
    
    # Found a new closer value
    if abs(target - closest) > abs(target - node.value):
        closest = node.value

    left = dfs(node.left, target, closest)
    right = dfs(node.right, target, closest)
    
    # Return the closer of the values returned by children
    if abs(target - left) > abs(target - right):
        return right
    return left