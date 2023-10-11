#Exercise 1: Write a Python program that prints the current date and time using the datetime module.

import datetime

theTimeRn = datetime.datetime.now()

#exp 1. imported datetime module and made a var called theTimeRn which references datetime using now functions to give the current date and time, printed the var


#Exercise 2: Write a Python program that prints the current date and time using the datetime module. Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)

print(theTimeRn.strftime("%D"))
print(theTimeRn.strftime("%T"))

#exp 2. referenced var called theTimeRn which references datetime using now functions to give the current date and time, printed the var and passed it through the function strftime with the "%D" and "%T" to get the current time and the date

#Exercise 3: Using the strptime function, convert two strings into dates. Then find the difference in days between the two.

typeYourDate = input("Type a date in DD/MM/YY order: ")

typeYourDate2 = input("Type another date in DD/MM/YY order: ")

print(typeYourDate.strftime("%j"))



"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""