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