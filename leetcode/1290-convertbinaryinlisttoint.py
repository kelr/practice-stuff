class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Convert each node in the list to a string and append it to an array. Join the array to a bitstring and convert it to an int.
# O(N) since single pass over the list + an O(N) string concat in join()
# O(N) space due to N elements in the result list and an N length string
def getDecimalValue(head: ListNode) -> int:
    result = [str(head.val)]
    curr = head.next
    while curr is not None:
        result.append(str(curr.val))
        curr = curr.next
    return int("".join(result), 2)

# Better method by just doing bit operations. Left shift the current value and or it with the current value.
# O(N) since single pass over the list
# O(1) space
def getDecimalValueShift(head: ListNode) -> int:
    curr = 0
    while head:
        curr = curr << 1 | head.val
        print(curr)
        head = head.next
    return curr

test = ListNode(1, ListNode(1, ListNode(0)))
assert getDecimalValue(test) == 6
getDecimalValueShift(test)
