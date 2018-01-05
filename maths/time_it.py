from functools import wraps
import time

def time_it(func):
    """
    Decorator for timing a function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_end = time.time()
        print ('Function: %r took %4.4f ms' % (func.__name__, (time_end - time_start) * 1000))
        return result
    return wrapper    