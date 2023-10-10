"""
Chapter 1 Exercise 3: Print Date and Time
Write a Python program to display the current date and time.
"""
#The code imports the "datetime" module, gets the current date and time, and finally prints it in a formatted string.

import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))