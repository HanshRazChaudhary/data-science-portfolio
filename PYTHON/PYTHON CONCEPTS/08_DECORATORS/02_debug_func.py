def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} : {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} With Arg {arg_value} and Kwargs {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("Halo")

@debug
def greet(name, greeting = "Namaste!"):
    print(f"{greeting}, {name}")

hello()
greet("Python", greeting="Hello") 