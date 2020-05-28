class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Swap each pair of adjacent nodes. 
# O(N) time where N is the number of nodes since there will be N/2 swaps
# O(1) space since no new nodes are created
def swapPairs(head: ListNode) -> ListNode:
    # Handle empty list
    if head is None:
        return None

    curr = head
    adj = curr.next

    # Handle a list with 1 node
    if adj is None:
        return head

    # We need to adjust the head node the first time so set a flag
    first = True

    while True:
        # Swap nodes, set a previous reference
        prev = curr
        curr.next = adj.next
        adj.next = curr

        if first:
            head = adj
            first = False

        # If the list has an even number of nodes, the current next will be None at the end
        if curr.next is None:
            return head

        # Move the pair pointers to the next pair
        curr = curr.next
        adj = curr.next

        # If the list has an odd number of nodes, adj will be None at the end
        if adj is None:
            return head

        # The previous curr has to point to adj now
        prev.next = adj


data = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

out = swapPairs(data)
while out is not None:
    print(out.val)
    out = out.next