#  Write a Python program which accepts the radius of a circle from the user and compute the area.

# first create a  variable and store the user input function .
# in eval function  we can give the value integer and float value .

a = eval(input("enter your circle radius : "))

# we know what is the formula of area of circle area = pie * (radius*radius) then we create a variable of area.
area = 22/7*(a*a)

print("area of circle : ",area)

''' output - 
 enter your circle radius : 14  . 
area of circle :  616.0 '''