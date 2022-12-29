''' Write a Python program to get file creation and modification date/times.'''

# first we import the  time module because we datetime
import time as t

# then we need os module ,why? , because to find the file path .
import os

a = r"C:\Users\This pc\PycharmProjects\pythonProjectw3\coding practise\codingpractice\Q-63.py"

# file modification time
b = os.path.getmtime(a)

d = t.ctime(b)


print("modification date/time : ",d)
# cretion file time
c = os.path.getctime(a)

d = t.ctime(c)
print("cretaion date/time : ",d)


