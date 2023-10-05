#Exercise 1: Write a program to print each character of a given string using a for loop

money = "real"

for reality in money:
    print(reality)

#created a var "money" with the value of the string "real" and a for loop that iterates through each character of the value of money using the var "reality" and prints them each on a seperate line.


#Exercise 2: Write a program to calculate the sum of elements in a list using a for loop.

real = [1010, 21, 400]

total = 0

for hunnit in range(0, len(real)):
    total = total + real[hunnit]
    print("Sum of all elements in given list: ", total)


#Created a list var and another var to be used for the total sum of the list values. For loop uses var "hunnit" to cycle through the list based on the starting point number its given("len" returns the number of items in the list) (0 is the first index, 1010, so I use that). 2nd line of for loop equates the value of each addition operation after the iteration of the operation. This repeats 3 times because there are 3 numbers in the list. 


#Exercise 3: Write a program to print the length of each word in a sentence using a for loop and a list.

theTing = input("Give me a word: ")

str_list = list(theTing.split(" "))

for theTings in ((str_list)):
    print(len(theTings))

#Created a var input to take in a sentence. Another var to split the input by the spaces the user writes in their senctence. For loop iterates though 2nd var based on how it recognizes characters other than the one called to in the split function and gives the length of each word in the sentence.



#Excercise 4: Write a program that creates a dictionary (atleast 4 key:value pairs) and then iterates through a dictionary and prints the result

#In a comment, answer the following, what do you notice about the output of your code. Is it what you expected?

mydict = {
  "real": "reality",
  "600": "6hunnit",
  "year": 2023,
  "fake": False
}

for zaDict in ((mydict)):
    print((zaDict))

#created a dict and then a for loop to cycle through it

#I noticed it only prints the keys and not their value pairs..