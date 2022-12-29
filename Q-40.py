'''Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)'''

import math as mt
x1=eval(input("enter your point x1: "))
y1=eval(input("enter your point x2 : "))
x2=eval(input("enter your point x2 : "))
y2=eval(input("enter your point y2 : "))

d = (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
print("Distance between two point : ",mt.ceil(d))
print(print("Distance between two point : ",(d)))
'''output -
enter your point x1: 2
enter your point x2 : 3
enter your point x2 : 4
enter your point y2 : 5
Distance between two point :  3

without ciel method ans is 
Distance between two point :  2.8284271247461903

'''