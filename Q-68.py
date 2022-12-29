'''Write a Python program to calculate sum of digits of a number.'''

'first take input user'
a = str(int(input("enter your number : ")))
'we are creating variable b to store the value'
b = 0
for i in a:
    b+=int(i) # whatever value come from for loop b+ variable add all the value and store the value in b

print("sum of digit number : ",b)

'''output -
enter your number : 1234
10
'''








