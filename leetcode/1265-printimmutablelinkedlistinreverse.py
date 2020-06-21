# Use a stack. Iterate through the list and push values onto the stack.
# Then pop values off the stack and print them.
# O(N) time, N to make the stack, N to pop
# O(N) space, N elements in the stack
def printLinkedListInReverse(head) -> None:
        stack = []
        while head:
            stack.append(head)
            head = head.getNext()
        
        while stack:
            stack.pop().printValue()

# Recursively print the list. 
# O(N) time, N recursive calls
# O(N) space, N recursive calls on the call stack
def printLinkedListInReverse(head) -> None:
    if head:
        printLinkedListInReverse(head.getNext())
        head.printValue()

# Get the list length, go to the last value, print it, 
# then go to the 2nd to last... etc until the first value is printed.
# O(N^2) time, N to get length + N + N-1 + N-2 + ... + 1 = N+N(N-1)/2
# O(1) space
def printLinkedListInReverse(head) -> None:
        curr = head
        length = 0
        while curr.getNext():
            length += 1
            curr = curr.getNext()
        
        while length >= 0:
            curr = head
            for _ in range(length):
                curr = curr.getNext()
            length -= 1
            curr.printValue()

# Get list length then use DnC to split the list in half.
# Continue splitting until there is 1 node in each split, then print from the right.
# O(NlgN) time, N to get list length + NlgN by the masters theorem for DnC.
# O(lgN) space, at most there are lg N saved half nodes
def printLinkedListInReverse(head) -> None:
    divide(head, getSize(head))

def getSize(head):
    size = 0
    while head:
        size += 1
        head = head.getNext()
    return size
    
# Print the upper halves first
def divide(head, n):
    if n > 1:
        half = head
        for _ in range(n // 2):
            half = half.getNext()
        divide(half, n - n // 2)
        divide(head, n //2)
    elif n != 0:
        head.printValue()