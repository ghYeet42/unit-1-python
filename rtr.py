#Exercise 1: Write a program to print numbers from 1 to 10 using a for loop.

for x in range(11):
    print(x)

#for loop with range of 11 to count to 10 when printed


#Exercise 2: Write a program to count by 10s from 900 to 1000 

for x in range(900, 1010, 10):
    print(x)

#for loop with range starting at 900, ending at 1010, and incrementing by 10 to count from 900 to 1000

#Exercise 3: Write a program that counts form 1-100 by 9

for x in range(1, 109, 9):
    print(x)

#same as previous but different numbers

#Exercise 4: Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.

m = 0

for x in range(1, 11):
    m += x
    print(m)

#created the variable m and then a for loop to iterate from 1-10 (range(1-11)) using var x and add x to m after every iteration so 0+1, 0+1+2, 0+1+2+3, etc.



#Excercise 5: Uncomment the following code and run it. Then answer the following: - What is the ouput of the code? - Explain the iterative process that this code executes to get that output


rows = 5

for i in range(rows):
    for j in range(i + 1):
         print('*', end=' ')
    print()

#the output is a row with just 1 star at first then each iteration  another is added until there is a row of 5 stars.

#the first for loop uses i to reference the range in the rows var and then the 2nd for loop, var j is used as reference to what is the star and the space that comes after it and is set to iterate by adding the "*" and the " " to the list each time to i until it reaches 5 which is what var rows is equal to.