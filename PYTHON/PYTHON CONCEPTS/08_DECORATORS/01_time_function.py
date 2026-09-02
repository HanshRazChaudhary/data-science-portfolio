import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"{func.__name__} Ran {stop - start} Time.")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(5)