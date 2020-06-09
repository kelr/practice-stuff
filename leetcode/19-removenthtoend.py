class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

# Find the length of the list, then go to the node behind the node to delete and delete it.
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    # Empty list
    if not head:
        return head
    # Non-positive n is an invalid input
    if n < 1:
        return None

    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next

    # No action needed if n is > len
    if n > length:
        return head

    # Delete the head if they are equal
    if n == length:
        return head.next

    curr = head
    for _ in range(length - n - 1):
        curr = curr.next
    curr.next = curr.next.next
    return head 

# Use two runner pointers. Fast advances n+1 distance away from the slow pointer.
# Then advance both pointers at the same time until fast hits the end.
# Slow will then be the node behind the node to be deleted, just delete next.
def removeNthFromEndSingle(head: ListNode, n: int) -> ListNode:
    if not head:
        return head
    if n < 1:
        return head

    fast = head
    slow = None
    # Get fast n distance away from slow. 
    for _ in range(n):
        if fast:
            fast = fast.next
        else:
            return head

    # Advance both pointers until fast reaches the end
    while fast:
        fast = fast.next
        if not slow:
            slow = head
        else:
            slow = slow.next

    # If slow is still None, means we gotta delete the head
    if not slow:
        return head.next

    slow.next = slow.next.next
    return head


test = ListNode(1, ListNode(3, ListNode(5, ListNode(3, ListNode(1)))))
res = removeNthFromEndSingle(test, 6)
while res:
    print(res.val)
    res = res.next
