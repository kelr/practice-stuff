class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        O(N) time, worst case is when we're getting the last index.
        O(1) space.
        """
        if index > self.size - 1:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        O(1) time, just make a new node and adjust the head pointer. 
        O(1) space.
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = self.head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        O(1) time, just make a new node and adjust the tail pointer. 
        O(1) space.
        """
        node = Node(val)
        self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = self.tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        O(N) time, worst case is adding at the 2nd to last index.
        O(1) space.
        """
        if index > self.size or index < 0:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.size += 1
            
        if not self.tail:
            self.tail = self.head

    def deleteAtIndex(self, index: int) -> None:
        """
        O(N) time, worst case is removing the last index.
        O(1) space.
        """
        if index > self.size - 1 or index < 0:
            return

        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

            if index == self.size - 1:
                self.tail = curr
        self.size -= 1
        if self.size == 0:
            self.tail = None
