class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterate through the list twice, create a new list and append all lesser values first, then values equal or greater
# O(N) time since there are 2N iterations through the list
# O(N) space, since a new list is created
def partition(head: ListNode, x: int) -> ListNode:
    out = ListNode()
    curr = head
    curr_out = out
    while curr:
        if curr.val < x:
            curr_out = append(curr_out, curr.val)
        curr = curr.next
    curr = head
    while curr:
        if curr.val >= x:
            curr_out = append(curr_out, curr.val)
        curr = curr.next

    return out.next

def append(node: ListNode, val: int) -> ListNode:
    if node:
        node.next = ListNode(val)
        node = node.next
    else:
        node = ListNode(val)
    return node
    

def partitionInPlace(head: ListNode, x:int) -> ListNode:
    curr = head
    before_head = ListNode()
    after_head = ListNode()
    before = before_head
    after = after_head
    
    while curr:
        if curr.val < x:
            before.next = curr
            before = before.next
        else:
            after.next = curr
            after = after.next
        curr = curr.next
    after.next = None
    before.next = after_head.next
    return before_head.next

test = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
res = partitionInPlace(test, 3)
while res:
    print(res.val)
    res = res.next


