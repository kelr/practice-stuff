class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Set the new head node as the minimum of the two input head nodes. Use l1 if they are equal. 
# Go to the next node of the list of the node that was chosen. Add the minimum val node as the next to the output node.
# Continue until either list is empty, in which case append the rest of the non empty list.
# Both lists cannot be empty unless they were input as empty since we add one node at a time.
# O(N) time where N is the total number of nodes since we add each node once.
# O(1) space since no new nodes are created
def mergeTwoLists(l1, l2) -> ListNode:
    # Deal with edge cases
    if l1 is None and l2 is not None:
        return l2
    if l1 is not None and l2 is None:
        return l1
    if l1 is None and l2 is None:
        return None

    # Set the first node as the minimum of the two head nodes
    out = None
    if l1.val <= l2.val:
        out = l1
        l1 = l1.next
    else:
        out = l2
        l2 = l2.next

    # Get another ref to the head node that we won't modify
    original = out

    while True:
        # If either of the two lists are empty, just append the rest of the non empty list
        if l1 is None and l2 is not None:
            out.next = l2
            break
        if l1 is not None and l2 is None:
            out.next = l1
            break
        if l1 is None and l2 is None:
            break

        # Set the next node as the minimum of the two potential nodes
        if l1.val <= l2.val:
            out.next = l1
            l1 = l1.next
            out = out.next
        else:
            out.next = l2
            l2 = l2.next
            out = out.next

    return original

one = ListNode(1, ListNode(2, ListNode(4)))
two = ListNode(1, ListNode(3, ListNode(4)))
out = mergeTwoLists(one, two)

while out is not None:
    print(out.val)
    out = out.next