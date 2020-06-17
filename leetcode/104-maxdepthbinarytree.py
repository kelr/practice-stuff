# Each node returns the sum of the greater of its childrens depths, plus its own.
# O(N) time, each node is traversed once
# O(N) space, worst case is a binary tree where each node has 1 children except the leaf causing N recursive calls on the stack.
def maxDepth(root) -> int:
    return 0 if not root else 1 + max(maxDepth(root.left), maxDepth(root.right))