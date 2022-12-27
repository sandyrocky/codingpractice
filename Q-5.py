# Write a Python program which accepts the user's first and \n
# last name and print them in reverse order with a space between them.

# first create  input user variable

fname  = input("Enter user your first name : ")

# then create second inupt user variable
lname  = input("Enter user your last name : ")

#then create third variable to store a and b varible in third variable  ,
# we concat two variable and also provide  space b/w two name .
c = lname + "  " + fname
# finally we print c .
print("aur bhai , ",c)


''' output - 
Enter user your first name : sandeep
Enter user your last name : yadav
aur bhai ,  yadav  sandeep
'''