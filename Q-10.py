''' Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.'''

n = int(input('enter a number :'))
s = int(f'{n}')
s1 = int(f'{n}{n}')
s2 = int(f'{n}{n}{n}')
print(s)
print(s1)
print(s2)
print ("The value is :",s+s1+s2)

'''output -
enter a number :8
8
88
888
The value is : 984
'''