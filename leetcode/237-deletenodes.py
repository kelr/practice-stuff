class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

# Question kinda succs. You can delete the node without the head
# by just copying the values of the next node.
# O(1) time and space
def deleteNode(node: ListNode) -> None:
    node.val, node.next = node.next.val, node.next.next

test = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))
deleteNode(test.next)
while test:
    print(test.val)
    test = test.next
