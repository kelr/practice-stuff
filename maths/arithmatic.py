def sum_items(iterable):
    s = 0
    for n in iterable:
        s += n
    return s

def product_items(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p