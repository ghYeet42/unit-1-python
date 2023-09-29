#1. Simple Counter: Write a program that uses a while loop to print numbers from 1 to 10.

i = 1
while i < 11:
  print(i)
  i += 1

#exp 1. Used plus-equal and set i to be 0 and the while condition to be i > 0, numbers print continuously until i no longer meets the condition of i < 11


#2. Countdown: Write a program that uses a while loop to print numbers from 10 to 1 in descending order.

i = 10
while i > 0:
  print(i)
  i -= 1

#exp 2. I did the same thing I did for task one except I used minus-equal and set i to be 10 and the while condition to be i > 0


#3. Factorial Calculation: Write a program that calculates the factorial of a given number using a while loop


num = 9
factorial = 1

while num > 1:
    factorial = factorial * num
    print(factorial)
    num -=  1
    
#exp 3. Made 2 variables, one for the factorial starting number, and where it will stop, set the while loop to run from 9 to 1 so it does 9 then 9x8 then 9x8x7, etc.


#4. Password Guessing Game: Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.

thePass = input("Guess the password: ")

while thePass != "moneyreal":
    if thePass == "moneyreal":
        print("You got it!")
    else:
        print("Thats not it..")
        break

#exp 4. Made an input variable and a while loop that says "Thats not it.." if the password is incorrect, if it is "You got it!" should print.


#5. Sum of Digits: Write a program that calculates the sum of the digits of a given number using a while loop.


num = (input('Enter a positive number: '))
for "1" in num or "2" in num or "3" in num or "4" in num or "5" in num or "6" in num or "7" in num or "8" in num or "9" in num :
    print("The sum of the digits in the number you've entered is: " + (num) + (num))
    break

#exp 5. Tried making an input and a loop that is supposed to look through the the characters of the input since its a string, convert them to integers and add them to eachother.

#6. Fibonacci Series: Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.

num1 = 1

num2 = 1

n = input("Enter a number to give a length to the seuqence: ")

listFib = []
print(num1)

while n >= 0:
    sequence = num1 + num2
    listFib.append(sequence)
    print(listFib)
    
    print(listFib[0] + listFib)
    num +=  1

#exp 6. Tried making a list and an input for how long the sequence should be. The program should append the values to the list and then continue trying appending values based on the 2nd newest value added to the newest value.