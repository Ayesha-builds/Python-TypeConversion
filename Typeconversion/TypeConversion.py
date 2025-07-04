# 1. Basic Input with Integer Conversion
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# ------------------------------

# 2. Multiple Inputs with Space Separation
x, y = map(float, input("Enter two floating-point numbers separated by space: ").split())
print("Product:", x * y)

# ------------------------------

# 3. Expression Evaluation with eval()
expr = input("Enter a mathematical expression (e.g. 3+5*2): ")
print("Result:", eval(expr))

# ------------------------------

# 4. List Input using eval()
lst = eval(input("Enter a list (e.g. [1, 2, 3, 4]): "))
print("Sum of list elements:", sum(lst))

# ------------------------------

# 5. Boolean Type Conversion
val = input("Enter any value to convert to boolean: ")
print("Boolean result:", bool(val))

# ------------------------------

# 6. String to Float Conversion
num_str = input("Enter a floating-point number as a string: ")
f = float(num_str)
print("Square:", f ** 2)

# ------------------------------

# 7. Dictionary Input using eval()
d = eval(input("Enter a dictionary (e.g. {'a': 1, 'b': 2}): "))
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))

# ------------------------------

# 8. List of Integers from Space Separated Input
nums = list(map(int, input("Enter integers separated by space: ").split()))
print("Maximum:", max(nums))
print("Minimum:", min(nums))

# ------------------------------

# 9. Mixed Type Literal Input with eval()
literal = eval(input("Enter any Python literal (e.g. 42, 'hello', [1,2], (1,2)): "))
print("Type:", type(literal))

# ------------------------------

# 10. Combined Type Conversion
int_input = int(input("Enter an integer: "))
float_input = float(input("Enter a float: "))
print("Sum:", int_input + float_input)
