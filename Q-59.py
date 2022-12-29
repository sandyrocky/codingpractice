''' Write a Python program to convert height (in feet and inches) to centimeters.'''

a = int(input("Enter height in feet : "))
b = int(input("Enter height in inches : "))
c = f'{a}'+f'{"feet"}'+","+f'{b}'f'{"inches"}'
print(c)
centimeter = ((a*12)+b)*2.54
print("Height converted to centimeter : ",centimeter, "cm")

'''output -
Enter height in feet : 5
Enter height in inches : 4
5feet,4inches
Height converted to centimeter :  162.56 cm
'''