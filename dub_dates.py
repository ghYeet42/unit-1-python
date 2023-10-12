#Exercise 1: Write a Python program that prints the current date and time using the datetime module.

import datetime

theTimeRn = datetime.datetime.now()

#exp 1. imported datetime module and made a var called theTimeRn which references datetime using now functions to give the current date and time, printed the var


#Exercise 2: Write a Python program that prints the current date and time using the datetime module. Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)

print(theTimeRn.strftime("%D"))
print(theTimeRn.strftime("%T"))

#exp 2. referenced var called theTimeRn which references datetime using now functions to give the current date and time, printed the var and passed it through the function strftime with the "%D" and "%T" to get the current time and the date

#Exercise 3: Using the strptime function, convert two strings into dates. Then find the difference in days between the two.

from datetime import datetime

string = "21 February, 2018"

string2 = "25 February, 2018"

object = datetime.strptime(string, "%d %B, %Y")

object2 = datetime.strptime(string2, "%d %B, %Y")

print(object2 - object)

#exp 3. imported datetime module and made 2 vars (string and string2) that hold dates, made 2 more vars (object and object2) that use datetime and strptime function to turn the strings into time formats for both object vars then printed object2 - object.


#Excercise 4: Write a program that asks the user for their birthdate and calculates their current age using the datetime module.

import datetime

from datetime import datetime

typeYourDate = input("Type your birthday in 'Day Month, Year' order (ex: 16 June, 2020): ")

typeYourDatee = datetime.strptime(typeYourDate, "%d %B, %Y")

print("You are" + typeYourDatee("%Y") - theTimeRn("%Y") + "years old.") 

#exp 4. imported datetime module(s) and made a var input typeYourDate and then another var, typeYourDatee, to convert the input into proper format and then subtract it from the var made previously, theTimeRn, to get the user's age