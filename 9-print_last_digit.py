def print_last_digit(number):
    if number < 0:
        number = abs(number)
    num = number % 10
    print("{}".format(num),end="")
    return num



print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
