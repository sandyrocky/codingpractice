''' Write a Python program to convert all units of time into seconds.'''

hour = int(input("Enter your hour : "))
minute = int(input("Enter your minute : "))

hour_to_sec = (hour*3600)
minute_to_sec = minute*60

sec = hour_to_sec + minute_to_sec

print("Hour and minute are converted : ",sec, " sec.")

'''output-
Enter your hour : 2
Enter your minute : 1
Hour and minute are converted :  7260  sec.
'''