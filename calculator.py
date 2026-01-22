#calculator.py
print("1. Create a calculator using functions")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print()
# --------------------------------------------------
print("2. Pass parameters and return values using function")
def square(n):
    return n * n
num = 6
print("Square of", num, "=", square(num))
print()
# --------------------------------------------------
print("3. Use default arguments in functions")
def power(base, exp=2):
    return base ** exp
print("Default power:", power(5))
print("Custom power:", power(5, 3))
print()
# --------------------------------------------------
print("4. Call functions based on user choice")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
choice = 1
a, b = 8, 3
if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", subtract(a, b))
else:
    print("Invalid choice")
print()
# --------------------------------------------------
print("5. Separate logic into multiple functions")
def input_numbers():
    return 4, 7
def add_numbers(x, y):
    return x + y
x, y = input_numbers()
print("Sum:", add_numbers(x, y))
print()
# --------------------------------------------------
print("6. Handle division by zero")
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print("Division:", safe_divide(10, 2))
print("Division:", safe_divide(10, 0))
print()
# --------------------------------------------------
print("7. Use docstrings in functions")
def greet(name):
    """Returns a greeting message"""
    return "Hello " + name
print(greet("Python"))
print()
# --------------------------------------------------
print("8. Test each function independently")
def test():
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(3, 4))
test()
print()
# --------------------------------------------------
print("9. Modular calculator program")
def calculator():
    a, b = 9, 3
    print("Add:", add(a, b))
    print("Subtract:", subtract(a, b))
    print("Multiply:", multiply(a, b))
    print("Divide:", divide(a, b))
calculator()