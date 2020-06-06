class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Create a hash map for all visited nodes, iterate a pointer through the list and add the node if its not in the map.
# If the node is in the map, the pointer has visited before and therefore there is a cycle.
# O(N) time, N iterations single pass through the list
# O(N) space, worst case every node is in the visited map which is N entries
def hasCycle(head: ListNode) -> bool:
    curr = head
    visited = {}
    
    while curr:
        if curr in visited:
            return True
        else:
            visited[curr] = True
        curr = curr.next
    return False

# Use two pointers, fast runs every iteration through the list and slow runs every other iteration. They start with fast ahead.
# If they ever meet, there is a cycle.
# O(N), N iterations if there are no cycle, if there is a cycle it takes at most K iterations for the slow runner to
# arrive at the cycle, then distance/speed cycles to reach, which is N + K
# O(1) space
def hasCycleNoMap(head: ListNode) -> bool:
    if not head:
        return False
    fast = head.next
    slow = head

    step = False
    while fast:
        if fast == slow:
            return True
        if step:
            slow = slow.next
        step = not step
        fast = fast.next
    return False
