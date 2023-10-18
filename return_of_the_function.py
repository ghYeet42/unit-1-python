#Task 1: Calculate the Square of a Number Write a function that takes an integer as an argument and returns its square.

import math

def sqrtOfNum(a):
    return math.sqrt(a)

real = sqrtOfNum(9)

print(real)

assert sqrtOfNum(9) == 3

try:
    assert sqrtOfNum == 4
except:
    print("(this is the try + except print statement speaking after 2nd assertion statement in the try proved false) Nah man, you're one off!")

#exp 1. imported math module and used sqrt function inside of the fucntion I made and then set var "real", added correct and incorrect assertions as application of unit testing practice as well as try and except statement for incorrect

#Task 2: Calculate the Area of a Rectangle: Write a function that takes the length and width of a rectangle and returns its area.

def calculate_area(length, width):
    airTheUhh = length * width
    return airTheUhh

reality = calculate_area(3000, 20)

assert reality == 60000

print(reality)

try:
    assert reality == 60001
except:
    print("(this is the try + except print statement speaking after 2nd assertion statement in the try proved false) Nah man, you're one off!")

#exp 2. Made calculate_area with "(length, width)" arg and a var that does length times width and then returned the var once, then called upon the the var which returns the function calculating the arg "(3000, 20)", added correct and incorrect assertions as application of unit testing practice as well as try and except statement for incorrect


#Task 3: Convert Temperature from Celsius to Fahrenheit: Write a function that takes a temperature in Celsius and returns  the equivalent temperature in Fahrenheit using the correct formula

def cToF(theCelsius):
    celsToFarTing = (theCelsius * 9/5) + 32
    return celsToFarTing

cToFPrint = cToF(45)

assert cToFPrint == 113

print(cToFPrint)

try:
    assert cToFPrint == 114
except:
    print("(this is the try + except print statement speaking after 2nd assertion statement in the try proved false) Nah man, you're one off!")

#exp 3. Made function cToF and then arg theCelsius, made var inside of function that calculates C to F then returned the var, mde another var that is stores parameter 45 (cToFPrint) of cToF function and printed that var, added correct and incorrect assertions as application of unit testing practice as well as try and except statement for incorrect


#Task 4: Calculate the Average of Numbers: Write a function that takes a list of numbers  and returns the average (mean) of those numbers.


def listAvg(lst):
    theAvgcalc = sum(lst)/len(lst)
    return theAvgcalc

heresTheAvg = listAvg([20, 30, 400, 50, 20120])

print(heresTheAvg)

assert heresTheAvg == 4124

try:
    assert heresTheAvg == 4125
except:
    print("(this is the try + except print statement speaking after 2nd assertion statement in the try proved false) Nah man, you're one off!")

#exp 4. Made function listAvg that calcs the mean of a list using sum and len functions inside of var theAvgcalc then made a var that holds the function I made and then printed the function, added correct and incorrect assertions as application of unit testing practice as well as try and except statement for incorrect
