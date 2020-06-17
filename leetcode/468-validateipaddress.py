# O(1) time and space, since IP address are bounded. Otherwise O(N) time, O(N) space since split makes a copy of the string.
def validIPAddress(IP: str) -> str:
    if isValidIPv4(IP):
        return "IPv4"
    if isValidIPv6(IP):
        return "IPv6"
    return "Neither"

def isValidIPv4(IP: str) -> bool:
    s = IP.split(".")
    if len(s) != 4:
        return False

    for num in s:
        if len(num) == 0 or len(num) > 3:
            return False
        
        # No leading zeroes
        if len(num) != 1 and num[0] == ("0"):
            return False

        # Numbers only
        if not num.isdigit():
            return False

        # Between 0 and 255
        if int(num) > 255:
            return False

    return True
    
def isValidIPv6(IP: str) -> bool:
    s = IP.split(":")
    if len(s) != 8:
        return False

    for num in s:
        # No leading zeroes or extra chars, no empty spaces
        if len(num) > 4 or len(num) == 0:
            return False

        # Validate hex string
        if not all(char in '0123456789abcdefABCDEF' for char in num):
            return False

    return True


isValidIPv4("172.16.254.1")