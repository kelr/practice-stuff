import sys
class ABBADiv1:
	"""
	A Binary Search Tree where node children survive only if their data string
	builds closer to a target string
	"""
	def __init__(self):
		self.root = None
		self.target = ""
		self.target_reverse = ""
		self.initial = ""

	def canObtain(self, initial, target):
		self.target = target
		self.target_reverse = target[::-1]
		self.initial = initial

		# Don't forget the root node
		if self.root is None:
			self.root = Node(self.initial)
		return "Possible" if self._check_and_insert(self.root) else "Impossible"

	def _check_and_insert(self, node):
		# If we reached the terminating length, see if the strings are equal
		if len(node.data) == len(self.target):
			if node.data == self.target:
				return True
			else:
				del node
				return False
		
		# If our current string can't be found in the target or the reverse target
		# Back up and try a different combination
		if node.data not in self.target and node.data not in self.target_reverse:
			del node
			return False

		# Construct new children nodes
		node.left = Node(self._moveA(node.data))
		node.right = Node(self._moveB(node.data))

		# Check both children nodes and their data
		return self._check_and_insert(node.left) or self._check_and_insert(node.right)

	def _moveA(self, string):
		return string + "A"

	def _moveB(self, string):
		string = string + "B"
		return string[::-1]

class Node:
	def __init__(self, data=None):
		self.data = data
		self.left = None
		self.right = None

if __name__ == '__main__':
	abba = ABBADiv1()
	print(abba.canObtain(sys.argv[1], sys.argv[2]))
