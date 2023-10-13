#Task 1: Calculate the Square of a Number Write a function that takes an integer as an argument and returns its square.

import math

def sqrtOfNum(a):
    return math.sqrt(a)

real = sqrtOfNum(9)

print(real)

#exp 1. imported math module and used sqrt function inside of the fucntion I made and then set var "real"

#Task 2: Calculate the Area of a Rectangle: Write a function that takes the length and width of a rectangle and returns its area.

def calculate_area(length, width):
    airTheUhh = length * width
    return airTheUhh

reality = calculate_area(3000, 20)

print(reality)

#exp 2. Made calculate_area with "(length, width)" arg and a var that does length times width and then returned the var once, then called upon the the var which returns the function calculating the arg "(3000, 20)"


#Task 3: Convert Temperature from Celsius to Fahrenheit: Write a function that takes a temperature in Celsius and returns  the equivalent temperature in Fahrenheit using the correct formula

def cToF(theCelsius):
    celstoFarTing = (theCelsius * 9/5) + 32
    return celstoFarTing

cToFPrint = cToF(45)

print(cToFPrint)

#exp 3. Made function cToF and then arg theCelsius, made var inside of function that calculates C to F then returned the var, mde another var that is stores parameter 45 (cToFPrint) of cToF function and printed that var


#Task 4: Calculate the Average of Numbers: Write a function that takes a list of numbers  and returns the average (mean) of those numbers.


lst = [20, 30, 400, 50, 20120]

def listAvg(lst):
    theAvgcalc = sum(lst)/len(lst)
    return theAvgcalc

heresTheAvg = (listAvg)

print(heresTheAvg)

#exp 3. Made function listAvg that calcs the mean of a list using sum and len functions inside of var theAvgcalc then made a var that holds the function I made and then printed the function
