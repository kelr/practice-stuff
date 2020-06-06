###########
# 2.1
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a freq map, iterate through the list. If the val appears as a key in freq, delete the node.
# O(N) time, single pass to iterate and delete all duplicates.
# O(N) space, worst case there are N freq entries if every value is unique
def removeDups(head: ListNode) -> ListNode:
    if not head:
        return head
    freq = {}
    curr = head
    freq[curr.val] = True
    
    while curr.next:
        if curr.next.val in freq:
            curr.next = curr.next.next
            continue
        else:
            freq[curr.next.val] = True
        curr = curr.next
    return head

# Use two pointers, fast is ahead of slow and iterates every subsequent node each time slow increments.
# If fast finds a value that matches slow, delete the fast node.
# O(N^2) time as there are N(N-1)/2 comparisons worst case
# O(1) space
def removeDupsNoFreq(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    
    slow = head
    fast = head
    while slow:
        while fast.next:
            if fast.next.val == slow.val:
                fast.next = fast.next.next
            else:
                fast = fast.next
        slow = slow.next
        fast = slow
    return head

test = ListNode(1, ListNode(3, ListNode(5, ListNode(3, ListNode(1)))))
test2 = None
test3 = ListNode(1)
test4 = ListNode(3, ListNode(3, ListNode(3, ListNode(3))))
res = removeDupsNoFreq(test4)
while res:
    res = res.next

def findKthToLast(head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    if k < 1:
        return None
    curr = head
    length = 0
    while curr:
        length += 1
        curr = curr.next
    if k > length:
        return None
    curr = head
    for _ in range(length - k):
        curr = curr.next
    return curr 

res = findKthToLast(test, 2)
print(res.val)
