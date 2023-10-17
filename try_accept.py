
try:
    age = int(input('Enter your age: '))
    faveNum = int(input('What is your favorite number: '))
except:
    print("Bruh, I'm only taking integers..")


if age <= 21:
    print('You are not allowed to enter, you are too young.')
else:
    print('Welcome, you are old enough.')
    
    
try:
    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except:
    print("unable to divide by zero")


#changed the line that has the print statement "print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)" and moved into try and based on if the user input was 0, it would do the exception statement, same for the inputs but if they recieve characters and not ints, they will run their exception statement