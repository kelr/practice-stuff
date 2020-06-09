class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next

# Find the length of the list and iterate to the middle
# O(N) time, N to find the length, floor(N/2) to get to the middle
# O(1) space
def middleNode(head: ListNode) -> ListNode:
    listLen = 0
    curr = head
    while curr:
        listLen += 1
        curr = curr.next
    
    mid = listLen // 2
    curr = head
    for _ in range(mid):
        curr = curr.next
    return curr

# Optimize away the time needed to search back through the list to the middle
# by keeping a map of positions.
# O(N) time, N iterations to find length and to fill the map
# O(N) space, all N elements in the list is in the map
def middleNodeFaster(head: ListNode) -> ListNode:
    positions = {}
    listLen = 0
    curr = head

    while curr:
        positions[listLen] = curr
        listLen += 1
        curr = curr.next
    
    return positions[listLen // 2]

# Use two runner pointers, if fast runs twice as fast as slow, when fast reaches the end
# slow will be at the middle. This is probably optimal.
# O(N), N/2 iterations
# O(1) space
def middleNodeFastest(head: ListNode) -> ListNode:
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

test = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
res = middleNodeFastest(test)
while res:
    print(res.val)
    res = res.next

test = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
res = middleNodeFastest(test)
while res:
    print(res.val)
    res = res.next

test = ListNode(1)
res = middleNodeFastest(test)
while res:
    print(res.val)
    res = res.next

test = ListNode(1, ListNode(2))
res = middleNodeFastest(test)
while res:
    print(res.val)
    res = res.next