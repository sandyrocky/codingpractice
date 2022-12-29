'''Write a Python program to print all even numbers from a given numbers list in the same order and
 stop the printing
if any numbers that come after 237 in the sequence.'''
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
            399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
            958,743, 527]

for n in numbers:
    if n==237: # it is fillter all the number
        print(n) # it is print only 237 before.
        break  # here  statement is stoped .

    elif n%2==0:
        print("it is even number : ",n)


'''output -
it is even number :  386
it is even number :  462
it is even number :  418
it is even number :  344
it is even number :  236
it is even number :  566
it is even number :  978
it is even number :  328
it is even number :  162
it is even number :  758
it is even number :  918
237'''
