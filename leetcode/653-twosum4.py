# DFS through the tree. Store the k-val compliment in the set if the val is not in the set.
# If val is in the set, return True as there is a pair that sum to the target.
# O(N) time, worst case checks every node.
# O(N) space, up to N values in the compliment set + potentially N calls on the stack.
# This is a BST, so could probably be more efficient.
compliments = set()
def findTarget(root, k):
    if root:
        if root.val in self.compliments:
            return True
        self.compliments.add(k - root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
    return False