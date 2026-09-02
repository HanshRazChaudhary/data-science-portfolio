# Scope
username = "PythonLezhand"

def name():
    username = "Python Legend"
    print(username)

print(username)
name()

x = 100

def func():
    x = 10
    return x + 10


print(func())

# Clouser Example
def test(num):
    def funct(x):
        return x ** num
    return funct

inp = test(3)
out = test(4)
print(inp(5))
print(out(6))