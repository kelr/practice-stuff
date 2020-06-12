import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = {}
        self.keyList = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        O(1) time due to new dict entry and list append.
        O(1) space.
        """
        if val in self.m:
            return False
        self.m[val] = len(self.keyList)
        self.keyList.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        O(1) time due to one pop for each of the dict and list
        """
        if val not in self.m:
            return False
        # Get the index for val and the key for the head of the list
        idx = self.m[val]
        head = self.keyList[-1]
        
        # Replace the to be deleted key with the head of the keylist.
        # Change the idx in the map for the head val to be the deleted idx
        self.keyList[idx] = head
        self.m[head] = idx
        
        # Delete the head from the keylist and the value from the map
        self.keyList.pop()
        self.m.pop(val, 0)
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        O(1) time since keylist is already a list and random.choice is O(1)
        """
        return random.choice(self.keyList)
