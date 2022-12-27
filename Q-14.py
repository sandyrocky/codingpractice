'''Write a Python program to calculate number of days between two dates.'''

# import date module
import datetime as dt

f_date = dt.date(2022, 12, 8)
l_date = dt.date(2022, 12, 27)
difference = l_date - f_date
print("Difference b/w two date  : ",difference.days,"days")

'''output -
Difference b/w two date  :  19 days'''