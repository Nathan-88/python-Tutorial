#  a function that removes all characters c and C from a string.
def no_c(my_string):
    str = ""
    for i in my_string:
        if (i == 'c') or (i == 'C'):
            continue
        str += i
    return (str)

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
