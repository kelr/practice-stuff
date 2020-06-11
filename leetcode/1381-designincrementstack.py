class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.curr_size = 0
        self.list = []

    # Push is O(1) amortized
    def push(self, x: int) -> None:
        if self.curr_size < self.max_size:
            self.list.append(x)
            self.curr_size += 1

    # Pop is O(1)
    def pop(self) -> int:
        if self.curr_size == 0:
            return -1
        self.curr_size -= 1
        return self.list.pop()

    # Increment is O(N) worst case when we have to increment everything
    def increment(self, k: int, val: int) -> None:
        for i, num in enumerate(self.list):
            self.list[i] += val
            k -= 1
            if k == 0:
                return