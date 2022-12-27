'''Write a Python program to get the difference between a given number and 17,
if the number is greater than 17 return double the absolute difference.
'''

n = int(input("Enter your number : "))
if n>17:
    print("number",n," is grater then 17 return double number  :", ((n-17)*2))
else:
    print("number",n ,"is less than 17 : ",(17-n))

