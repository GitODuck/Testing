# TabCode Git demo - Python file
# Push this to GitHub, then edit a line and push again to show the diff.

def greet(name):
    return f"Hello, {name}! Welcome to the TabCode review."

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    print(greet("Reviewers"))
    print("First 10 Fibonacci numbers:", fibonacci(10))
