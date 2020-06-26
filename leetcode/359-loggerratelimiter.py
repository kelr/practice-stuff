
# Use a hash map to store seen messages with their timestamps. If a message has been seen before within 10s
# return false, else true. 
# O(1) time, each call is just a hash map lookup
# O(N) space, the hash map can grow to the size of every unique message which can be bad.
class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message in self.history:
            if timestamp - self.history[message] < 10:
                return False
        self.history[message] = timestamp
        return True


# Use a queue along with a hash map to garbage collect messages that are older than 10s.
# Sacrifices some time to ensure that memory usage does not grow unbounded. Can run GC in a diferent thread
# if the queue and history are protected.
# O(N) time, garbage collection in the worst case can delete the entire queue, and since messages can arrive
# at the same timestamp, the max size of queue and the hash map is how many unique messages arrive within 10s N.
# O(N) space, queue and hash map can be a max size of N unique messages that arrived within the last 10s.
from collections import deque
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.history = {}
        self.queue = deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        # Run garbage collection on messages older than 10s.
        while self.queue:
            msg = self.queue[0]
            # If this message expired, remove it
            if timestamp - self.history[msg] >= 10:
                self.queue.popleft()
                del(self.history[msg])
            else:
                break
                
        # If the message is in the history, it must be within 10s.
        if message not in self.history:
            self.history[message] = timestamp
            self.queue.append(message)
            return True
        else:
            return False