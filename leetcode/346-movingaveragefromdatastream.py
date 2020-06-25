
# 5:41
# Maintain a queue and calculate the average each step.
# O(N) time, where N is size. calculating the average is linear, insertion is O(1) and queue with a list is a O(N) insert.
# O(N) space, where N is size
def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.size = size
        

def next(self, val: int) -> float:
    if len(self.queue) == self.size:
        self.queue.pop(0)
    print(val)
    self.queue.append(val)
    return reduce(lambda x,y: x+y, self.queue) / len(self.queue)


from collections import deque
# 3:09
# Use a deque for constant time inserts and pops. Maintain a current sum
# of all the elements in the queue. If an element is popped, subtract that from the current sum.
# Add the new element to the current sum and return the average.
# O(1) time, deque inserts and pops are O(1), adjusting the average is O(1)
# O(N) space, where N is size
def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.size = size
        self.currSum = 0
        

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.currSum -= self.queue.popleft()
            
        self.queue.append(val)
        self.currSum += val
        return self.currSum / len(self.queue)