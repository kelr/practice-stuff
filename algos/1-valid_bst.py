#!/usr/bin/python

# Verify that a BST is valid

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def check_subtree(node, curr_min, curr_max):
    """ Helper function to recursively check that a subtree is valid.
        Validity is defined as all left child nodes < current and all right child nodes > current.

        Args:
            node- Current node
            curr_min- Current minimum node value so far
            curr_max- Current maximum node value so far
        Return:
            bool- valid or not
    """
    # Base case. Also BSTs that don't exist are valid.
    if node is None:
        return True

    # Val must be less than the saved minimum and greater than the saved max
    if node.val <= curr_min or node.val >= curr_max:
        return False

    if not check_subtree(node.left, curr_min, node.val):
        return False

    if not check_subtree(node.right, node.val, curr_max):
        return False

    return True

def is_valid_bst(root):
    return check_subtree(root, float("-inf"), float("inf"))

def test():
    # 1 level test
    node = TreeNode(5)
    node.left = TreeNode(4)
    node.right = TreeNode(7)
    assert is_valid_bst(node)

    # Test 2 levels
    node2 = TreeNode(8)
    node2.left = TreeNode(5)
    node2.left.left = TreeNode(3)
    node2.left.right = TreeNode(6)
    node2.right = TreeNode(20)
    node2.right.left = TreeNode(17)
    node2.right.right = TreeNode(100)
    assert is_valid_bst(node2)

    # Test single subtree not a bst
    node3 = TreeNode(8)
    node3.left = TreeNode(5)
    node3.left.left = TreeNode(3)
    # This one should be > 5
    node3.left.right = TreeNode(4)
    node3.right = TreeNode(20)
    node3.right.left = TreeNode(17)
    node3.right.right = TreeNode(100)
    assert not is_valid_bst(node3)

    # Single node
    node4 = TreeNode(5)
    assert is_valid_bst(node4)

    # Unbalanced
    node5 = TreeNode(5)
    node5.left = TreeNode(4)
    assert is_valid_bst(node5)

    node6 = TreeNode(5)
    node6.right = TreeNode(6)
    assert is_valid_bst(node6)

    node7 = TreeNode(5)
    node7.right = TreeNode(1)
    assert not is_valid_bst(node7)

    # Empty
    node7 = None
    assert is_valid_bst(node)

if __name__ == '__main__':
    test()
