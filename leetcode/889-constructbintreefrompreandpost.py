class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Maintain two indexes, one for pre and one for post.
# Create the root node which is guaranteed to be the first val in pre.
# Recursively check if the current node is not the current val in post,
# then either create the left child or the right child.
# If the node is the current val in post, it means we are done with the node
# and should return from the recursion, so just increment the post idx.
# O(N) time where N is the length of pre + the length of post.
# O(N) space, output tree will have N new nodes where N is the length of pre or post.
def constructFromPrePost(self, pre, post):
    self.preIdx = 1
    self.postIdx = 0
    root = TreeNode(pre[0])
    self.rec(root, pre, post)
    return root
    
    
def rec(self, node, pre, post):     
    if node.val != post[self.postIdx]:
        node.left = TreeNode(pre[self.preIdx])
        self.preIdx += 1
        self.rec(node.left, pre, post)
        
    if node.val != post[self.postIdx]:
        node.right = TreeNode(pre[self.preIdx])
        self.preIdx += 1
        self.rec(node.right, pre, post)
        
    self.postIdx += 1