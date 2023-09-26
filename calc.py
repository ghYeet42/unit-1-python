print("Welcome to the calculator")

#printed calculator welcome statement\

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
print()
print("Select operation: 1. Addition 2. Subtraction 3. Multiplication 4. Division 5. Floor Division 6. Exponential 7. Remainder: ")
print()
opSelect = (input("Enter your choice: "))

#created 3 inputs, 2 for taking numbers, 1 for selecting operation type and a print statement (empty prints for spacing), str on the opSelect inout variable because for later is in the if conditional statements

#a = 123
 
#b = 'Hello'

#print('Is a an instance of str?', isinstance(a, str))
#print('Is b an instance of str?', isinstance(b, str))

if isinstance(opSelect, int) == False:
    print()
    print()
    print("You cannot!")
    print()
    print()

# created a an if statement to check if what input choice was an integer using "isinstance", if so then the program proceeds based on the correlation of the number you input from 1 to 7


if int(opSelect) == 1:
        print(num1 + num2)
elif int(opSelect) == 2:
    print("Your first input subtracted from your second input is: ")
    print(num1 - num2)
    print("Your second input subtracted from your first input is: ")
    print(num2 - num1)
elif int(opSelect) == 3:
        print(num1 * num2)
elif int(opSelect) == 4:
    print("The quotient of your first input divided by your second input is: ")
    print((num1 / num2))
    print("The quotient of your second input divided by your first input is: ")
    print((num2 / num1))
elif int(opSelect) == 5:
    if num1 == 0:
        print("You can't divide by zeor buddy..")
    elif num2 == 0:
        print("You can't divide by zeor buddy..")
    else:
        print("The quotient of your second input floor-divided into your first is: ")
        print((num1 // num2))
        print("The quotient of your first input floor-divided into your second is: ")
        print((num2 // num1))
elif int(opSelect) == 6:
    print("Your first input to the power of your second input is:")
    print(num1 ** num2)
    print("Your second input to the power of your first input is:")
    print(num2 ** num1)
elif int(opSelect) == 7:
    print("The remainder of your first input divided by your second input is: ")
    print(num1 % num2)
    print("The remainder of your second input divided by your first input is: ")
    print(num2 % num1)
else:
        print("You cannot!") # if number isn't from 1 to 7, you should get this


#created a conditional that checks the input value of the opSelect input from 1 to 7 and performs the operation(s) corelated to said number. Number 1 is addition (the "+" sign), number 2 is subtraction, etc.