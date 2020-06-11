# Push open parens onto the stack and pop closed parens.
# Push parens to the output string unless the stack was empty prior to a push
# or if the stack becomes empty after a pop. These are the outer parens to remove.
# O(N) time, single pass through the string
# O(N) space, about N/2 space for the stack and at most N-2 space for the output string
# since input S is considered to always be a valid parens string.
def removeOuterParentheses(S: str) -> str:
    out = []
    stack = []
    for char in S:
        if stack and char == "(":
            out.append(char)
        if char == "(":
            stack.append(char)
        else:
            stack.pop()
            if stack:
                out.append(char)
    return "".join(out)

# Uses less space
def removeOuterParenthesesRefactor(S: str) -> str:
    out = []
    num_open_parens = 0

    for char in S:

        if char == "(" and num_open_parens > 0:
            out.append(char)
        if char == ")" and num_open_parens > 1:
            out.append(char)

        if char == "(":
            num_open_parens += 1
        else:
            num_open_parens -= 1
    return "".join(out)

assert "()()()" == removeOuterParenthesesRefactor("(()())(())")