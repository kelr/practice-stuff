
# O(Q*N) time, where Q is the average length of a query string and N is the number of queries.
# O(N) space, N elements for the output bool array
def camelMatch(queries, pattern: str):
    out = []
    for q in queries:
        out.append(match(q, pattern))
    return out
            
# Compare a char in query to a char in pattern. If they match, increment both and continue until either
# pattern is done iterating or query is done iterating. 

# If the values don't match, keep iterating query but stop iterating pattern. This is handling all the extra
# lowercase chars inbetween the uppercase chars in query. If they match again, continue iterating both.

# If the chars dont match but query is an uppercase char, that means there is no way pattern can be built into query
# since we cannot insert uppercase letters, so return false.

# If query is done iterating but pattern is not, it means that query is either shorter than pattern or
# there was a mismatch that never resolved. In either case, theres no way pattern can turn into query so return False

# O(Q) time, at most iterates through all of queries chars of len Q.
# O(1) space
def match(query, pattern):
    if len(pattern) > len(query):
        return False
    i = 0
    for char in query:
        if i < len(pattern) and char == pattern[i]:
            i += 1
        elif char.isupper():
            return False
    return i == len(pattern)


# Insert oo and ar
assert match("FooBar", "FB")

# Insert o and a
assert match("FooBar", "FoBr")

# Can't insert capital T
assert not match("FooBarT", "FB")

# Same string
assert match("a", "a")

# Insert a
assert match("a", "")

# Can't insert capital F
assert not match("F", "")

# Len pattern is > len query
assert not match("", "a")

# Len pattern is > len query
assert not match("", "F")