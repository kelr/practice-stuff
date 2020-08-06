def hasPathSum(root, sum) -> bool:
    return dfsBranchSum(root, 0, sum)

# Perform DFS and maintain a running sum on the path to a leaf node.
# If the node is a leaf, check if the running sum equals the target and return True if so
# else, check and return children if they are true or not.
# O(N) time, visits every node
# O(N) space, worst case there are N recursive calls on the call stack for a unbalanced tree where its a linked list
def dfsBranchSum(node, currSum, targetSum):
    if not node:
        return False

    currSum += node.val

    # If this is a leaf node, check sum
    if not node.left and not node.right:
        return currSum == targetSum
    
    return dfsBranchSum(node.left, currSum, targetSum) or dfsBranchSum(node.right, currSum, targetSum)