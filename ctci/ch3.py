##### 3.3
class SetOfStacks:
    def __init__(self, cap):
        self.capacity = cap
        self.stacks = {}
        self.curr_stack = 0

    def _curr_len(self) -> int:
        return len(self.stacks[self.curr_stack])

    def show(self) -> None:
        for i in range(self.curr_stack+1):
            if i in self.stacks:
                print(self.stacks[i])

    def push(self, val: int) -> None:
        if self.curr_stack in self.stacks:
            if self._curr_len() >= self.capacity:
                self.curr_stack += 1
                self.stacks[self.curr_stack] = [val]
            else:
                self.stacks[self.curr_stack].append(val)
        else:
            self.stacks[self.curr_stack] = [val]

    def pop(self) -> int:
        # Find the closest non-empty stack
        while self.curr_stack not in self.stacks:
            if self.curr_stack == 0:
                return None
            self.curr_stack -= 1

        val = self.stacks[self.curr_stack].pop()
        # Go to the previous non-empty stack if the current one became empty
        if self._curr_len() == 0:
            del(self.stacks[self.curr_stack])
            while self.curr_stack not in self.stacks:
                if self.curr_stack == 0:
                    return val
                self.curr_stack -= 1
        return val

    def popAt(self, index: int) -> int:
        val = None
        if index in self.stacks:
            val = self.stacks[index].pop()
            if len(self.stacks[index]) == 0:
                del(self.stacks[index])
        return val

s = SetOfStacks(4)
for i in range(16):
    s.push(i)

for i in reversed(range(16)):
    assert i == s.pop()
assert None == s.pop()

for i in range(16):
    s.push(i)

# Pop out the stack at index 1
assert 7 == s.popAt(1)
assert 6 == s.popAt(1)
assert 5 == s.popAt(1)
assert 4 == s.popAt(1)
assert None == s.popAt(1)

# Check that pop correctly skips over the missing index 1
for i in reversed(range(8, 16)):
    assert i == s.pop()
for i in reversed(range(4)):
    assert i == s.pop()
assert None == s.pop()