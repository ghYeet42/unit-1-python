tdolist = []

#empty todo list set to being a variable called "tdolist" that is a list

tdo = input("Do you want to add or delete a todo? TYPE d/a: ")

#user input to add or subtract a todo

while True:
    if tdo == "a": #if state for deleting todos
        print()
        real = input("Write what do you want to add: ") #variable made for adding todos
        print()
        tdolist.append(real) #the user's input is appended to their todo list (tdolist variable)
        print()
        print ("Your updated list is: " + str(tdolist))
        print()
        tdo = input("Do you want to add or delete a todo? TYPE d/a: ")
        print()
    elif tdo == "d": #elif for deleting todos
        print()
        fake = input("Type the number of the item you want to delete: ") #variable made for adding todos
        print()
        del tdolist[int(fake) - 1] #removes the specific item in place of the INDEX of the number that the user input. Subtract 1 from the number that the user inputs and you get the index of the item they wish to remove.
        print()
        print ("Your updated list is: " + str(tdolist)) #prints updated list
        print()
        tdo = input("Do you want to add or delete a todo? TYPE d/a: ")
        print()
    elif tdolist == [] and tdo == "d": #this is supposed to stop the user from trying to delete from an empty list..
        print("You can't do that!")
        break
        
#while loop iterates through the processes of adding or deleting items