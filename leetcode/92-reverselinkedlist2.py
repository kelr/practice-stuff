class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Iterate 2 runner nodes 1 node apart until curr reaches m.
# Set 2 more pointers to fix the ending pointers afterward
# Reverse each node pair n - (m-1) times.
# Fix the end pointers with the 2 saved pointers.
# O(N) single pass through the list
# O(1) space
def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    
    if not head or  m == n or not head.next:
        return head

    curr = head
    prev = None

    for _ in range(m-1):
        prev = curr
        curr = curr.next
    
    to_curr = curr
    to_prev = prev

    for _ in range(n-(m-1)):
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    if to_prev:
        to_prev.next = prev
    else:
        head = prev

    to_curr.next = curr
    
    return head

test = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))
res = reverseBetween(test, 2, 4)
while res:
    print(res.val)
    res = res.next


