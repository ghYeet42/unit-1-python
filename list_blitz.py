
# Task 1: Create a list with 4 elements and print it.

fourTings = [21, False, "money", "real"]

print(fourTings)

# exp 1: I created a list with 4 elements and printed it.

#########################

#Task 2: Add Element to a List Add an element to the end of the list. Print the updated list.

fourTings.append(True)

print(fourTings)

# exp 2: I added an element to my list and printed the updated list.

#########################

#Task 3: Remove Element from a List Remove a specific element from the list. Print the updated list.

fourTings.remove("money")

print(fourTings)

# exp 3: I remove money from the list and printed the updated list.

#########################


# Task 4: Modify Element in a List Modify an element at a specific index with a new value. Print the updated list.

fourTings[3] = "money"

print(fourTings)

# exp 4: I modified the 4th thing in the list (index value 3) of the list and printed the updated list.

#########################


# Task 5: Append Multiple Elements to a List Append multiple elements to the end of the list. Print the updated list.

fourTings.append("MORE MONEY")
fourTings.append("moneyreal")

#fourTings.extend(whateverwhatever)

print(fourTings)

# exp 5: I append multiple elements to the list and printed the updated list.

#########################



#Task 6: Delete Element at a Specific Index Delete an element at a specific index. Print the updated list.

del fourTings[3]

print(fourTings)

# exp 6: I deleted the alement at index 3 in the list and printed the updated list.

#########################



#Task 7: Subsetting lists Create a new variable equal to the first 2 items of your list Then print out the new variable
fourTingsSs = ["4hunnid", 69]

print(fourTingsSs)

# exp 7: I created a new variable equal to the first 2 items of my list and then printed out the new variable.


#########################



#Task 8: Extend a List Extend the list with the elements of another list. Print  the updated list.

fourTinga = fourTings + fourTingsSs

print(fourTinga)

# exp 8: I extended the list with the elements of the other list and printed the updated list.

#########################
