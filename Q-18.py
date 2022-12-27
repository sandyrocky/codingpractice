''' Write a Python program to calculate the sum of three given numbers,
 if the values are equal then return three times of their sum.'''


a = int(input("enter your first number : "))
b = int(input("enter your second number : "))
c = int(input("enter your third number : "))
d = a+b+c
if a==b==c:
    print(d*3)
else:
    print(d)
