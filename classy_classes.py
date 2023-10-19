"""
class Person:
    species = "humanb"

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def hi(self):
        print("Hi my name is " + self.name)

forlenza = Person()

forlenza.hi

class Teacher(Person):
    role = "teacher"
    def hi(self):
        print("Hi my name is Mr. " + self.name)

forlenza = Teacher("Forlenza", 184)
"""

#Task 1: People Class Define a class called Person with attributes name and age. Then, write a method within the class to introduce the person with their name and age. Create a new object using this new class, and call the method you created.

class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def hi(self):
        print("Hi my name is " + self.name)

somebody = Person("Carter", "17")

print(somebody.name)
print(somebody.age)

#created class Person and init'd it wtih parameters of name and age and then made a method called hi and made it say "Hi my name is " + sel.name, then I made a obj called somebody and set it to Person class with parameters of Carter and 17 then printed


#Task 2: Animals Speak Create a base class Animal with a empty method called speak. Then create two subclasses, Dog and Cat, each with their own speak method. Create objects using these subclasses and call the speak method.

class Animal:

    def __init__(self, speak) -> None:
        self.speak = speak

animal = Animal("Hi, I'm talking to ya!")

#created base class of Animal to be used for inheritence of its properties with later classes, has an empty method (or function) called speak


class Animal2(Animal):

    def speak():
        print("Hi, I talk as well!")

#used parent class of Animal to inherit its properties and use in class Animal 2

animal = Animal2

print(Animal2.speak())

#changed animal obj to be set to Animal2 class and printed obj with parameter of Animal2's method speak


class Animal3(Animal):

    def speak():
        print("Hi, I talk too!")
    
animal = Animal3

#used parent class of Animal to inherit its properties and use in class Animal3

print(animal.speak())

#changed animal obj to be set to Animal3 class and printed obj with parameter of Animal3's method speak



#Task 3: Banking Create a class BankAccount with attributes balance and owner. Include methods for depositing and withdrawing money, which should modify the balance attribute. Test these methods with instances of the class.



class BankAccount:

    def __init__(self, balance, owner):
        self.balance = balance
        self.owner = owner


    def nomoney(balance):
        nomoner = input("How much do you want to withdraw: ")
        yourmoner = balance - nomoner
        print("Your balance is: " + yourmoner)

    def yesmoney(balance):
        yesmoner = input("How much do you want to withdraw: ")
        yourmoner = balance + yesmoner
        print("Your balance is: " + yourmoner)



#made a class called bank account init'd with attributes of balance and owner and then 2 methods for depositing and withdrawing money
