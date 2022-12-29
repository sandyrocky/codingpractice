''' Write a Python program to sum of two given integers.
However, if the sum is between 15 to 20 it will return 20'''

def sum_of_two_number(a, b):
    sum = a + b

    if sum>=15 and sum<=20:
        return 20
    else:
        return sum

print("sum of two number which is less than and greater than 20 : ",sum_of_two_number(12,9))
print("sum of two number is equal to : ",sum_of_two_number(12,4),".because its sum is equall to 15 b/w 20.")

'''output -
sum of two number which is less than and greater than 20 :  21
sum of two number is equal to :  20 .because its sum is equall to 15 b/w 20.

'''