
# Push all opening parens to a stack, pop off the stack and look for a match if a closing parens is encountered.
# O(N) time where N is the number of characters in the string due to a single pass
# O(1) space
def isValid(s: str) -> bool:
    char_stack = []
    char_map = {
        "(" : ")",
        "{" : "}",
        "[" : "]"
    }

    for char in s:
        if char in char_map.keys():
            char_stack.append(char)
        else:   
            # Closing parens with no corresponding opening
            if len(char_stack) == 0:
                return False

            # Check that the latest opening parens matches the current closing
            if char != char_map[char_stack.pop()]:
                return False

    # Check if there are any hanging open parens
    return True if len(char_stack) == 0 else False

print(isValid('()[]{}'))