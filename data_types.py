
#TASK 1: Create a float variable, and then convert it to an integer. Print both the original variable and the converted integer.

x = 12.7

print(int(x))

print(x)

#exp 1: I created a float variable, and then convert it to an integer. Then I printed both the original variable and the converted integer.

########

#TASK 2: Write code that takes a number as input and prints whether it's positive, negative, or zero using if-elif-else statements.

posNeg = int(input("Give me a positive or negative number: "))

if (posNeg == 0):
    print("Your number is  0")
elif (posNeg < 0):
    print("Your number is negative")
else:
    print("Your number is positive")

#exp 2: I created a variable that requires user input then I made an if statement with one elif for numbers that are less than or greater than 0 and then 0 itself. Statements about the values of the input number ar to print accordingly based on user input being pos, neg or zero.

########

#TASK 3: Write code that takes two numbers as input (an integer and a float), performs addition, subtraction, multiplication, and division, and prints the results.

num1 = int(input("Give me a number: "))
num2 = int(input("Give me another number: "))

print(num1 + num2)

print(num1 - num2)

print(num1 / num2)

print(num1 * num2)

#exp 3: I created 2 input variables (converted to integers with int) and then I set them to print the answers of them added, subtracted, divided, and multiplied.  

########

#TASK 4: Create a dictionary with keys as fruit names and values as their respective quantities. Then print out the quantity of one of the fruits.

friuts = {
  "apple": 16,
  "banana": 12,
  "kiwi": 8
}

print (friuts["apple"])
print (friuts["banana"])
print (friuts["kiwi"])

#exp 4: I made a dictionary called friuts and printed each key value calling upon them one by one from the dictionary.

########

#TASK 5: Create a string variable with that is a list of numbers and convert that string into a tuple. Then print out the both the original string and tuple.

string1 = ("1 2 3 4 5 6 7")

struple = string1.split(" ")

struple = tuple(string1.split(" "))


print (string1)

print (struple)

#exp 5: I created a string variable and then another variable that converted the previous one to a tuple using the split function. Then I printed both.

########

friuts2 = [10, 20, 30, 40, 50, 60]

print(friuts2[2]) #[-1] print 5
print(friuts2[1]) # print 4
print(friuts2[0:1]) #[:1][0] print 23
print(friuts2[0:2]) #[1][:212] print 23 and 4
print(friuts2[1:3]) # print 4 and 5

print(str(friuts2) + str(friuts))

print(friuts2[1:5])

print(10 // 3)

