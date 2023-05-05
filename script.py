import sys

print(sys.executable)
print(sys.version)

def greet(who):
    greeting = f"Hello, {who}!"
    return print(greeting)


greet("Chu Hoang Minh Ngoc")
