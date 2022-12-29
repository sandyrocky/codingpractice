'''Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years'''

a = int(input("Enter your principal amount : "))
b = int(input("Enter your interest rate : "))
c = int(input("enter your year : "))

s_i = a*b*c/100

future_value = a+s_i

print("Your future value is  : ",future_value)

'''output -
Enter your principal amount : 1000
Enter your interest rate : 2
enter your year : 1
future value :  1020.0

'''