''' Write a Python program to get the least common multiple (LCM) of two positive integers.'''

from math import lcm

a = int(input("enter your first number : "))
b = int(input("enter your second number : "))
c = abs(a)
d = abs(b)
e = lcm(a,b)
print("Here is your least common multiple (LCM) : ",e)

'''output -
enter your first number : 12
enter your second number : 24
Here is your least common multiple (LCM) :  24

'''