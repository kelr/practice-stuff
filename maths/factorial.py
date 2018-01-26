def factorial(n):
    if n < 0:
        print("Input must be a non negative integer please")
        return
    if n <= 1:
        return 1
    curr = 1
    for i in range(n, 1, -1):
        curr *= i
    return curr