"""
Have the user enter their investment amount and expected interest
Each year investment will increase by thier investment + their investment * interest rate
print out the earnings after a 10 year period
"""
#Ask for money invested + the interest rate
money = input("How much to invest: ")
interest_rate = input("interest rate: ")
#convert the value to a float
money = float(money)
#convert to a float and round the value by 2digits
interest_rate = float(interest_rate)/100
#circle through 10years using a for loop and range for 1 - 9
for i in range(10):
    money = money + (money * interest_rate)

#result
print("Amount after 10years of compound interest is: {:.2f}".format(money))