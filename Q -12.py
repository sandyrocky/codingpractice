
'''Write a Python program to print the calendar of a given month and year.'''

import calendar as cl

month = int(input("enter your month :"))
year = int(input("enter your year : "))

print(cl.month(year , month))

'''output -
enter your month :12
enter your year : 2022
   December 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31
'''