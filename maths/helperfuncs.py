def ceiling(n):
    return int(n) if int(n) == n or n < 0 else int(n)+1

def floor(n):
    return int(n) if int(n) == n or n >= 0 else int(n)-1
