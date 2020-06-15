# Recurse through the tree and determine its maximum depth. Then recurse through it again
# with pre-order DFS and sum all the nodes that are at the maximum depth.
# O(N) two passes through the tree for 2N.
# O(N) space, at worst the tree could be N levels deep meaning N recursive calls on the stack.
def deepestLeavesSum(root) -> int:
    maxDepth = findMaxDepth(root, 0)
    return findSum(root, 0, maxDepth)
    
def findMaxDepth1(node, depth):
    if node:
        left = findMaxDepth(node.left, depth + 1)
        right = findMaxDepth(node.right, depth + 1)
        return max(left, right)
    return depth - 1

def findSum1(node, depth, target):
    if node:
        if depth == target:
            return node.val
        leftSum = findSum(node.left, depth+1, target)
        rightSum = findSum(node.right, depth+1, target)
        return leftSum + rightSum
    return 0



# Similar to above but using a single pass pre-order DFS through the tree. Maintain an array where the indicies
# represent the sum of the nodes per level. Add to the list as the tree is traversed.
# The sum of the deepest level is the last element in the sum list.
# O(N) single pass through the tree of N nodes
# O(N) space, at worst the tree could be N levels deep meaning N recursive calls and N sum elements.
def deepestLeavesSumSinglePass(root) -> int:
    if not root:
        return 0
    sums = []
    findSum(root, 0, sums)
    return sums[-1]
    
def findSum(node, depth, sums):
    if node:
        try:
            sums[depth] += node.val
        except:
            sums.append(node.val)
        findSum(node.left, depth + 1, sums)
        findSum(node.right, depth + 1, sums)


# Maintain a list of the previous, current and next levels of the tree.
# If the current level is empty, the sum must be the sum of the previous level nodes.
# O(N) time, every node is visited
# O(N) space, every level list has in total N elements.
def deepestLeavesSumList(root) -> int:
    currLevel = [root]
    while currLevel:
        nextLevel = []
        for node in currLevel:
            for child in [node.left, node.right]:
                if child:
                    nextLevel.append(child)
        prevLevel, currLevel = currLevel, nextLevel
    return sum(node.val for node in prevLevel)