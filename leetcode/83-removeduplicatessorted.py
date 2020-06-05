class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Use two pointers, if fast is the same as slow, increment fast until it no longer is. 
# Then set the next node on slow to the different value on fast, which skips duplicate values.
# O(N) time, fast iterates N times
# O(1) space, no extra space is used
def deleteDuplicates(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    slow = head
    fast = head.next
    
    while fast:
        if fast.val == slow.val:
            fast = fast.next
        else:
            slow.next = fast
            slow = slow.next
            fast = fast.next
    # If there were duplicates at the end of the list, fast would be None, so manually set slow.next once more
    slow.next = fast
    return head


test = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
res = deleteDuplicates(test)
while res:
    print(res.val)
    res = res.next


