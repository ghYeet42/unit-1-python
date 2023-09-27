
# Exercise 1: Check if an integer is even and greater than 10. Return True if both conditions are met, False otherwise.

number1 = bool(input("Type a number and if it meets the conditions, I'll print 'True', if not, 'False'."))

if number1%2 == 0 and number1 > 10:
  print(True)
else:
  print(False)

#exp 1: I created an if statement that checks whether or not the remainder of a number is 0 after its divided by 2 and if its greater than 10. If so, "True" is printed, if not, "False" is printed.


#Exercise 2: Determine the ticket price based on age and student status. Price is $10 if under 18 or a student, $20 otherwise.

yourAge = (input("Enter your age here for your ticket distribution: "))

studentCheck = (input("Are you a student (y/n): "))

if int(yourAge) < 18 or studentCheck == "y":
  print("Your ticket will cost $10.")
else:
  print("Your ticket costs $20.")

#exp 2: I created 2 inputs for age and whether or not someone is a student. If someone is a student, they automatically pay are ellidgible for the $10 ticket, if they are under 18 as well. If they are over 18 and are a student as well. I they are over 18 but aren't a student, they pay $20.


#Exercise 3: Prompt the user to enter a fruit name. Check if the fruit is in the list. If it is, print "Yes, that fruit is in the list." If it's not, print "No, that fruit is not in the list."

friutName = input("Type a friut you like: ")

fruits = ["tangerine", "orange", "blueberry"]

if friutName in fruits == "tangerine" or "orange" or "blueberry":
  print("Yes, that fruit is in the list.")
else:
  print("No, that fruit is not in the list.")

#exp 3: I created an inputl, a list of friuts, and an if statement to check if the input matches any of the friuts in the list. If so, "Yes, that fruit is in the list." is printed, if not, "No, that fruit is not in the list." is not.

#Exercise 4: Check if a year is a century year and a leap year.

year = int(input("Give me a year: "))

if year % 4 == 0 and year % 100 == 0:
   print("That's a leap year and a century year!")
else:
   print("That's not a leap year or a century year..")

#exp 4: I created a variable input and then a conditional that checks whether the input year has a remainder or not after being divided by 4 as well as 100. If so, the year is a leap year and century year, otherwise its not.



#Exercise 5: Calculate the cost of shipping for an online order based on the order weight and destination zone. The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. If the order weight is less than 0 kg, return an error message.


weight = input("Order weight in kilograms: ")

zone = input("Order Zone (A/B): ")

if zone == "A":
   print(weight * 5)
elif zone == "B":
      print(weight * 7)

#Exercise 6: Determine the type of a triangle based on side lengths. Equilateral, Isosceles, Scalene, or Not a triangle.

a = input("Enter side 1: ")
b = input("Enter a base: ")
c = input("Enter side 2: ")

if a >= b and b >= c:
  print("That's and scalene triangle")
elif a >= c and c >= b:
    print("That's and scalene triangle")
elif a >= c and c >= b:
    print("That's and scalene triangle")
elif c >= a and a >= b:
    print("That's and scalene triangle")
elif c >= b and b >= a:
    print("That's and scalene triangle")
elif b >= a and a >= c:
    print("That's and scalene triangle")
elif b >= c and c >= a:
    print("That's and scalene triangle")
else:
   if a and b > c:
      print("That's and scalene triangle")


#exp 6: I created 3 variable for taking the 3 sides of a triangle. Then I made an if statement setting certain parameters to print out whether the sides equate to either an equilateral, isosceles, scalene triangle or not a triangle at all.