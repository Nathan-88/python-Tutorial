#A function that prints a string in uppercase
def uppercase(str):
    new_str = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i)-32)
        new_str += i
    return new_str


print(uppercase("Best School"))
print(uppercase("Chicago"))
print(uppercase("C is fun!"))
print(uppercase("School"))
print(uppercase("Python"))
    

#uppercase("best")
#uppercase("Best School 98 Battery street")
