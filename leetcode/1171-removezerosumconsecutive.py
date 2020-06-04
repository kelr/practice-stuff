class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a map for running sum values to node pointers. If the sum is ever found again, set the node in the map's next value to the next value of the curr node.
# Essentially deleting the sublist that has the zero sum.
# If total sum is zero, head has to move to the new head.
# Restart from the head node if any deletions were made, as the deletion may create a new possible zero sum sublist.
# O(N) time maybe, a deletion can be at least 2 nodes but it would not have to iterate to the end to find them. 
# O(N) space, since at worst the map has an entry for each running sum if they are unique
def removeZeroSumSublists(head: ListNode) -> ListNode:
    if not head:
        return None
    if not head.next:
        return None if head.val == 0 else head

    nodeMap = {}
    currSum = 0
    curr = head
    while curr:
        currSum += curr.val
        if currSum == 0:
            head = curr.next
            curr = curr.next
            nodeMap.clear()
            currSum = 0
        elif currSum in nodeMap:
            nodeMap[currSum].next = curr.next
            nodeMap.clear()
            curr = head
            currSum = 0
        else:
            nodeMap[currSum] = curr
            curr = curr.next
    return head

test = ListNode(1, ListNode(2, ListNode(3, ListNode(-3, ListNode(-2))))) 
result = removeZeroSumSublists(test)
while result:
    print(result.val)
    result = result.next
