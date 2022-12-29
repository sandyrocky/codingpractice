'''Write a Python program to concatenate all elements in a list into a string and return it.'''

# first we create function
def conacat_string(l):
    a=""
    for x in l:
        a+=str(x)

    return a

print(conacat_string([1,2,3,4]))

'''output -
1234'''