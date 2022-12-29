'''Write a Python program to convert the distance (in feet) to inches, yards, and miles'''

feet = int(input("Enter distance  in feet : "))
'1 feet = 12 inches'
inches = (feet*12)
'1 feet = 0.33333 yards'
yards = (feet*0.33333)
' 1feet = 0.0001894'
miles = (feet*0.0001894)

print("feet converted in inches : ",inches)
print("feet converted in yards : ",yards)
print("feet converted in miles : ",miles)

'''output -
Enter distance  in feet : 5
feet converted in inches :  60
feet converted in yards :  1.6666500000000002
feet converted in miles :  0.0009469999999999999
'''

