class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution with DFS.
# O(N) time, visits every node
# O(lgN) space, most recursive calls is the height of the trees of lgN
def isSameTree(p, q) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False

    if p.val != q.val:
        return False
    
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Iterative solution with BFS and queue.
# O(N) time, visits every node
# O(lgN) space, most space the queue uses is the height of the trees or lgN
from collections import deque
def isSameTreeIter(p, q) -> bool:
    queue = deque([(p, q),])

    while queue:
        p, q = queue.popleft()

        if p and not q:
            return False
        if q and not p:
            return False

        if p and q:
            if (p.val != q.val):
                return False

            queue.append((p.left,q.left))
            queue.append((p.right, q.right))
    return True


