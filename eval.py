"""
The eval() function in Python is a built-in function that parses a string expression and evaluates it as a Python expression.
"""
# Example 1: Evaluating mathematical expressions
expression = "2 + 3"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")

# Example 2: Executing code from a string
x = 10
expression = "x + 5"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")

# Example 3: Creating dynamic variables
var_name = "2 +"
result = eval(var_name + " 10")
print(f"The value of the dynamically created variable var_name is: {result}")

# Example 4: Dynamic execution of functions
def add(a, b):
    return a + b


expression = "add(2, 3)"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")

"""
The exec() function in Python is a built-in function that executes arbitrary Python code contained in a string. This can be useful when you want to dynamically execute code or create new objects, such as variables or functions, from within your program.
"""
#Here is an example of how you could use the exec() function:
# Example 1: Creating dynamic variables
var_name = "foo"
exec(var_name + " = 10")
print(f"The value of the dynamically created variable '{var_name}' is: {foo}")
