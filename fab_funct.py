# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

def greet(name):
    print("Hello " + name + "!")

greet("John")

#exp 1. Made function greet with name arg, and prints "Hello " and then the name then "!" then called upon greet saying with arg "John"


# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

def sum_numbers(a, b):
    print(a+b)

sum_numbers(200,40)

#exp 2. Made function sum_numbers with name arg "(a, b" and prints the sum of the 2 numbers and called upon it passing the arg "(200, 40") output 240


# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(n):
    factorial = 1

    while n > 1:
        factorial = factorial * n
        print(factorial)
        n -=  1

factorial(5)

#exp 3. Made function factorialInator, one for the factorial starting number, and where it will stop, set the while loop to run from that number to that same number of times ran.


# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def is_even(num):
    if num / 2 == 0:
        print(True)
    else:
        print(False)

is_even(4)

#exp 4. Made function is_even with "(num)" arg and an if statement that checks if num arg is equal to 0 after division by 2 and prints true, else false, called upon function using are "(3)"


# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.


def calculate_area(length, width):
    airTheUhh = length * width
    print(airTheUhh)

calculate_area(3000, 20)

#exp 5. Made calculate_area with "(length, width)" arg and a var that does length times width and then printed the var, then called upon the functions with arg "(3000, 20)"
