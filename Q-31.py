'''Write a Python program to compute the greatest common divisor (GCD) of two positive integers.'''

from math import gcd

a = int(input("enter your first number : "))
b = int(input("enter your second number : "))
c = abs(a)
d = abs(b)
e = gcd(a,b)
print("Here is your greatest common divisor(GCD) : ",e)

'''output -
enter your first number : -12
enter your second number : -28
Here is your greatest common divisor(GCD) :  4
'''