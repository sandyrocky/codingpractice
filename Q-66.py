''' Write a Python program to calculate body mass index.'''

'formula of body mass index (BMI)'
' BMI = weight/height*2'

# take height input
Height = eval(input("enter your Height in feet  : "))
# take inch input
Inch = eval(input("enter your inch : "))
#converted height into feet and plus the inch input.
feet_into_inch = (Height*12+Inch) # 1 feet = 12inch
# square the feet_into_ inch
sq_height = feet_into_inch**2
# weight input
weight = eval(input("enter your weight : "))
# weight converted into pound
pound =  weight*2.20642
# calculate the BMI
BMI = (pound/sq_height)*703

print("Calculate the BMI : ",BMI)


'''output - 
enter your Height in feet  : 6
enter your inch : 2
enter your weight : 70
Calculate the BMI :  19.827963513513513

'''