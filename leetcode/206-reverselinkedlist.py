class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# Iterate through the list with 2 pointers, fast pointer is one node ahead of slow. Set fast to point to slow, then advance to the next two nodes.
# O(N) since there are N-1 iterations through the list.
# O(1) space
def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    fast = head.next
    slow = head
    slow.next = None
    while fast:
        tmp = fast.next
        fast.next = slow
        slow = fast
        fast = tmp

    return slow

# Same as above but recursively. 
# O(N) since there are N next swaps done
# O(N) space since there are N recursive calls on the call stack
def reverseListRec(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    return reverseRecursive(None, head)

def reverseRecursive(node1: ListNode, node2: ListNode) -> ListNode:
    if not node2.next:
        node2.next = node1
        return node2
    tmp = node2.next
    node2.next = node1
    return reverseRecursive(node2, tmp)

test = ListNode(1, ListNode(2, ListNode(3)))
result = reverseListRec(test)

while result:
    print(result.val)
    result = result.next
