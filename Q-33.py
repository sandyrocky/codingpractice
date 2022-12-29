'''Write a Python program to sum of three given integers. However,
if two values are equal sum will be zero'''


def sum_of_three_number(a, b, c):
    sum = a + b + c

    if a == b:
        return 0
    elif a==c:
        return 0
    elif b==c:
        return 0
    else:
        return sum



print("sum of three number : ",sum_of_three_number(23,2,14))
print("sum of three number : ",sum_of_three_number(23,23,14))

'''output -
sum of three number :  39
sum of three number :  0
'''
