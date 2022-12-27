'''Write a Python program to get a string which is n (non-negative integer) copies of a given string'''

'''we can take input  and we are going to create input function and store its values in variable '''
a = input("enter your string : ")
'''how many times do you want to print your string ,give here number'''
b = int(input("eter your number: ",))
c = a*b
print("you copied your string",b, "times  : " ,c)

'''output -
enter your string : asd
eter your number: 2
you copied your string 2 times  :  asdasd
'''