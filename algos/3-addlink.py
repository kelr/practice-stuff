"""
Add two numbers as a singly linked list

Ex:
342 + 465 = 807

LL representation:
2 -> 4 -> 3
5 -> 6 -> 4
=
7 -> 0 -> 8

"""


class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None

""" 
Both are O(N) where N is the size of the larger list or just the size of any if theyre the same. 
    Space is O(N) where N is the size of the larger list or just the size of any if theyre the same 
        since its a new node each iteration/recursion. Recursive solution stores state on the call stack.
"""
class Solution:
    def add_two(self, list1, list2):
        return self.add_two_recursive(list1, list2, 0)

    # Return Node object or None
    def add_two_recursive(self, node1, node2, carry):
        # Base case with no carry
        if node1 is None and node2 is None and carry == 0:
            return None

        # Handle last carry over
        if node1 is None and node2 is None and carry == 1:
            return Node(1)

        # If list 2 is longer
        if node1 is None:
            sum, carry = self.sum_and_carry(0, node2.val, carry)
            result = Node(sum)
            result.next = self.add_two_recursive(node1, node2.next, carry)
            return result

        # If list 1 is longer
        elif node2 is None:
            sum, carry = self.sum_and_carry(node1.val, 0, carry)
            result = Node(sum)
            result.next = self.add_two_recursive(node1.next, node2, carry)
            return result

        # Neither lists are none
        sum, carry = self.sum_and_carry(node1.val, node2.val, carry)
        result = Node(sum)
        result.next = self.add_two_recursive(node1.next, node2.next, carry)
        return result

    # Returns tuple of sum, carry
    def sum_and_carry(self, val1, val2, carry_in=0):
        sum = val1 + val2 + carry_in
        if sum >= 10:
            sum = sum % 10
            carry = 1
        else:
            carry = 0
        return sum, carry

    # Iterative solution
    def add_two_iter(self, node1, node2):
        curr1 = node1
        curr2 = node2
        carry = 0
        prev_node = None
        root = None

        while curr1 is not None and curr2 is not None:
            val, carry = self.sum_and_carry(curr1.val, curr2.val, carry)
            new_node = Node(val)
            if prev_node is not None:
                prev_node.next = new_node
            else:
                root = new_node
            prev_node = new_node
            curr1 = curr1.next
            curr2 = curr2.next


        if curr1 is None:
            val, carry = self.sum_and_carry(0, curr2.val, carry)
            new_node = Node(val)
            if prev_node is not None:
                prev_node.next = new_node
            else:
                root = new_node
            prev_node = new_node
            curr2 = curr2.next

        elif curr2 is None:
            val, carry = self.sum_and_carry(curr1.val, 0, carry)
            new_node = Node(val)
            if prev_node is not None:
                prev_node.next = new_node
            else:
                root = new_node
            prev_node = new_node
            curr1 = curr1.next


        # last carry
        if carry:
            new_node = Node(carry)
            if prev_node is not None:
                prev_node.next = new_node

        return root




l1 = Node(9)
l1.next = Node(9)
l1.next.next = Node(9)
l1.next.next.next = Node(9)

l2 = Node(9)
l2.next = Node(9)
l2.next.next = Node(9)

answer = Solution().add_two(l1, l2)
while answer:
  print(answer.val, end=' ')
  answer = answer.next
print()
answer = Solution().add_two_iter(l1, l2)
while answer:
  print(answer.val, end=' ')
  answer = answer.next