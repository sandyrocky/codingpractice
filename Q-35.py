'''Write a Python program that will return true
if the two given integer values are equal or their sum or difference is 5.'''

a = int(input("enter your number : "))
b = int(input("enter your number : "))

if a==b or a+b==5 or b-a ==5:
    print("true")

else:
    print("false")

'''output - 1.
enter your number : 22
enter your number : 21
false

2. 
enter your number : 3
enter your number : 2
true'''