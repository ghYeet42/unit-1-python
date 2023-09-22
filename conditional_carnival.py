
#TASK 1 Even or Odd Determine if a number is even or odd.

number = int (input ("Type a whole number: "))

if (number%2) == 0:
  print ()
  print ("Your number is even.")

  #if (number%4) == 0:
    #print ()
    #print ("Your number is divsibible by 4.")
  
else:
  print ()
  print ("Your number is odd.")


#print ()
#check = input ("Give me a 2rd whole number: ")

#print ()

#num = input ("Give a 3rd whole number: ")


#if int (num) % int (check) == 0:
  #print ()
  #print (check + " divides equally into " + num)
#else:
  #print ()

#exp 1: I created an if statement that checks whether or not the remainder of a number is 0 after its divided by 2. If so, its even, if not, it's odd.

#TASK 2 Positive, Negative, or Zero: Determine if a number is positive, negative, or zero.

posNeg = int(input("Give me a positive or negative number: "))

if (posNeg == 0):
    print("Your number is  0")
elif (posNeg < 0):
    print("Your number is negative")
elif (posNeg > 0):
    print("Your number is positive")
else:
    print("That's not a number!")



#exp 2: I created a variable that requires user input then I made an if statement with one elif for numbers that are less than or greater than 0 and then 0 itself. Statements about the values of the input number ar to print accordingly based on user input being pos, neg or zero. I also incorporated the isdigit

#EXTRA CREDIT: Tell the user if they did not enter a valid number


#TASK 3: Largest of Three Find and print the largest of three numbers.

w = input("Give me a number: ")
x = input("Give me another number: ")
y= input("Give me one more number: ")

biggestBird = max(w, x, y)

print(biggestBird)

#exp 3: I created 3 variable inputs and then a variable that checks the largest number of the 3 inputs using max and then printed the number.


#TASK 4: Leap Year Determine if a year is a leap year or not.

year = int(input("Give me a year: "))

if year % 4 == 0:
   print("That's a leap year!")
else:
   print("That's not a leap year.")

#exp 4: I created a variable input and then a conditional that checks whether the input year has a remainder or not after being divided by 4. If so, the year is a leap year, otherwise its not.



#TASK 5: Vowel or Consonant: Identify if a character is a vowel or consonant.

sumn = input("Give me a letter: ")

if (sumn == 'a','A' or sumn == 'e','E' or sumn == 'i','I' or sumn == 'o','O' or sumn == 'u','U' ):
        print("That's a vowel.")
else:
        print("That's a consonant.")

#exp 5: I created a variable input and then a conditional that checks whether the input is a vowel and prints so. If not, what will be printed is that the letter is a consonant.

#EXTRA CREDIT: Tell the user if they did not enter a valid letter
