''' Write a Python program to convert seconds to day, hour, minutes and seconds. '''

# we import the datetime modules
import datetime as dt

# first we take input from the user
a = eval(input("enter your second here : "))

# we  define dt constractor then we define the timedelta constructor ,timedelta take parameter of seconds
# and timedelta equall to the a variable .
b = dt.timedelta(seconds=a)
print(b)

'''output -
enter your second here : 122415567.55667
1416 days, 20:19:27.556670
'''
