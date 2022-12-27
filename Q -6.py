'''Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.'''


values = input("enter your number with comma - separated : ")
list = values.split(",")
tuple = tuple(list)

print('list , ',list)
print('tuple ,',tuple)

'''output -
enter your number with comma - separated : 1,2,3,4,5,6
list ,  ['1', '2', '3', '4', '5', '6']
tuple , ('1', '2', '3', '4', '5', '6')
'''