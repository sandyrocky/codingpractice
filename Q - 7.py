'''Write a Python program to accept a filename from the user and print the extension of that.'''

a = input("enter your file name : ")
extension = a.split(".")
print("output -" , extension[-1])

'''output - 
enter your file name : abc.python
output - python
'''