# Just do the level traversal from top to bottom and reverse the output.
# O(N), O(N)
def levelOrderBottom(root):
    out = []
    level = [root]
    while root and level:
        out.append([node.val for node in level])
        level = [kid for node in level for kid in (node.left, node.right) if kid]
    return out[::-1]


# Same as top to bottom but just insert it into the output in reversed order.
# O(N), O(N)
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    def rec(node, level, out):
        if node:
            # Create a new level if needed
            if len(out) == level:
                out.insert(0, [])
            out[len(out)-(level + 1)].append(node.val)
            rec(node.left, level + 1, out)
            rec(node.right, level + 1, out)

    if not root:
        return []

    out = []
    rec(root, 0, out)
    return out