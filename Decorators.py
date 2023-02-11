#Closures 
"""
def outername(msg):
    message = msg
    def innername():
        print("{}".format(message)) #message variable is called a free variable
    return innername # this returns a function to a variable so when the variable is called it prints the output
    #return innername() #this will return the free variable message

name = outername("Hi")
my_name = outername("chigoziem")
name()
my_name()
"""
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function # its the same as display = decorator_function(display) then u call the function display() after the line
def display():
    print("Ebuka created this")
# display = decorator_function(display)
display()
# if the function has an arg passed into it, it will give an error unless we pass in the *args in our wrapper function
@decorator_function
def variab(name, age):
    print(f"my name is {name} and my age is {age}")
variab("john", 12)