'''Write a Python program to print out a set containing all the colors from color_list_1
which are not present in color_list_2'''

color_list_1 =["red","yellow","white","green"]
color_list_2 = ["black","blue","green"]
# we are converting color_list_1 and color_list_2 , to store the values in a and b variable.

a = set(color_list_1)
b = set(color_list_2)
# we create new variable to store the value of set and to find the difference between two set values.
c = a.difference(b)
# we are converting set into list .
d = list(c)
print("these  color are not presented in color_list_2 : ",d)

'''output -
these  color are not presented in color_list_2 :  ['yellow', 'white', 'red']
'''