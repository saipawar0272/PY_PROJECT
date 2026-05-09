#OOPS assignment

"""1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter radius of circle: "))

c = Circle(r)

print("Area of circle:", c.area())
print("Perimeter (Circumference) of circle:", c.perimeter())

#------------------------------------------------------------------
"""2. Write a Python program to create a person class. 
Include attributes like name, country and date of birth. Implement a method to determine the person's age."""

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob should be in 'YYYY-MM-DD' format

    def calculate_age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")

        age = today.year - birth_date.year

        # Adjust age if birthday has not occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age


# Example usage
name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")

p = Person(name, country, dob)

print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.calculate_age())

#---------------------------------------------------------------------

"""3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations."""

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b

c = Calculator()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", c.add(num1, num2))
print("Subtraction:", c.subtract(num1, num2))
print("Multiplication:", c.multiply(num1, num2))
print("Division:", c.divide(num1, num2))

"""4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
 Implement subclasses for different shapes like circle, triangle, and square."""

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side



class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

c = Circle(5)
s = Square(4)
t = Triangle(6)

print("Circle -> Area:", c.area(), "Perimeter:", c.perimeter())
print("Square -> Area:", s.area(), "Perimeter:", s.perimeter())
print("Triangle -> Area:", t.area(), "Perimeter:", t.perimeter())

#---------------------------------------------------------------------------------

"""Write a Python program to create a class representing a binary search tree. 
Include methods for inserting and searching for elements in the binary tree."""





#--------------------------------------------------------------------------------------

"""6. Write a Python program to create a class representing a stack data structure.
 Include methods for pushing and popping elements.
"""





#-----------------------------------------------------------------------------------------

"""7.Write a Python program to create a class representing a linked list data structure. 
Include methods for displaying linked list data, inserting and deleting nodes."""


#--------------------------------------------------------------------------------

"""8. Write a Python program to create a class representing a shopping cart. 
Include methods for adding and removing items, and calculating the total price. """

class ShoppingCart:
    def __init__(self):
        self.items = {}   # Dictionary to store items {item_name: price}

    # Method to add item
    def add_item(self, name, price):
        self.items[name] = price
        print(f"{name} added to cart.")

    # Method to remove item
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"{name} removed from cart.")
        else:
            print(f"{name} not found in cart.")

    # Method to calculate total price
    def calculate_total(self):
        total = sum(self.items.values())
        print(f"Total price: {total}")
        return total

    # Method to display cart items
    def display_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            print("Items in cart:")
            for name, price in self.items.items():
                print(f"{name}: {price}")



"""9. Write a Python program to create a class representing a stack data structure.
 Include methods for pushing, popping and displaying elements."""


""""10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.
"""
#--------------------------------------------------------------------------------------------------------------------------

"""
11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
	Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
	Create a constructor with parameters: accountNumber, name, balance.
	Create a Deposit() method which manages the deposit actions.
	Create a Withdrawal() method which manages withdrawals actions.
	Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
	Create a display() method to display account details. Give the complete code for the BankAccount class."""


class BankAccount:

    # Constructor
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    # Withdrawal Method
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Bank Fees Method (5%)
    def bankFees(self):
        fee = self.balance * 0.05
        self.balance -= fee
        print(f"Bank fees of {fee} applied.")

    # Display Method
    def display(self):
        print("\nAccount Details:")
        print("Account Number:", self.accountNumber)
        print("Account Holder Name:", self.name)
        print("Balance:", self.balance)
#----------------------------------------------------------------------------------

"""12. Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

	Example 1:

	Approach:

	Create a class named FlashCard.
	Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
	Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
	Now prompt the user to answer the color of the randomly chosen fruit.
	If correct print correct else print wrong.
	Output:

	welcome to fruit quiz
	What is the color of Strawberries
	pink
	Correct answer
	Enter 0, if you want to play again: 0
	What is the color of watermelon
	green
	Correct answer
	Enter 0, if you want to play again: 1"""

import random


class FlashCard:

    def __init__(self):
        self.fruits = {
            "Banana": "yellow",
            "Strawberries": "pink",
            "Watermelon": "green",
            "Apple": "red",
            "Orange": "orange"
        }

    def play(self):
        print("welcome to fruit quiz")

        while True:
            fruit, color = random.choice(list(self.fruits.items()))

            answer = input(f"What is the color of {fruit} : ")

            if answer.lower() == color.lower():
                print("Correct answer")
            else:
                print("Wrong answer")
                print("Correct color is", color)

            choice = input("Enter 0, if you want to play again: ")

            if choice != "0":
                break


obj = FlashCard()
obj.play()

#--------------------------------------------------------------------

"""13. TechWorld, a technology training center, wants to allocate courses for instructors. An instructor is identified by name, technology skills, experience and average feedback. An instructor is allocated a course, if he/she satisfies the below two conditions:

	eligibility criteria:
	if experience is more than 3 years, average feedback should be 4.5 or more
	if experience is 3 years or less, average feedback should be 4 or more
	he/she should posses the technology skill for the course
	Identify the class name and attributes to represent instructors. Write a Python program to implement the class chosen with its attributes and methods.

	Note:

	Consider all instance variables to be private and methods to be public.
	An instructor may have multiple technology skills, so consider instance variable, technology_skill to be a list.
	check_eligibility(): Return true if eligibility criteria is satisfied by the instructor. Else, return false
	allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false.
	Represent a few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program."""

class Instructor:

    def __init__(self):
        self.__name = None
        self.__technology_skill = []
        self.__experience = 0
        self.__average_feedback = 0

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_technology_skill(self, technology_skill):
        self.__technology_skill = technology_skill

    def set_experience(self, experience):
        self.__experience = experience

    def set_average_feedback(self, average_feedback):
        self.__average_feedback = average_feedback

    # Getter methods
    def get_name(self):
        return self.__name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience

    def get_average_feedback(self):
        return self.__average_feedback

    # Method to check eligibility
    def check_eligibility(self):

        if self.__experience > 3 and self.__average_feedback >= 4.5:
            return True

        elif self.__experience <= 3 and self.__average_feedback >= 4:
            return True

        else:
            return False

    # Method to allocate course
    def allocate_course(self, technology):

        if self.check_eligibility() and technology in self.__technology_skill:
            return True

        else:
            return False


# Object 1
i1 = Instructor()

i1.set_name("Sai")
i1.set_technology_skill(["Python", "Java", "SQL"])
i1.set_experience(5)
i1.set_average_feedback(4.7)

print("Instructor Name:", i1.get_name())

if i1.allocate_course("Python"):
    print("Course Allocated")
else:
    print("Course Not Allocated")


print()


# Object 2
i2 = Instructor()

i2.set_name("Rahul")
i2.set_technology_skill(["C", "C++"])
i2.set_experience(2)
i2.set_average_feedback(3.8)

print("Instructor Name:", i2.get_name())

if i2.allocate_course("Python"):
    print("Course Allocated")
else:
    print("Course Not Allocated")


"""
14. Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product.
 The program must display the years, months and days that are left for expiry."""

from datetime import datetime

class Product:

    def __init__(self, mfg_date, exp_date):

        self.mfg_date = datetime.strptime(mfg_date, "%d-%m-%Y")
        self.exp_date = datetime.strptime(exp_date, "%d-%m-%Y")

    def expiry_details(self):

        today = datetime.today()

        if self.exp_date < today:
            print("Product is already expired")

        else:
            diff = self.exp_date - today

            days_left = diff.days

            years = days_left // 365
            months = (days_left % 365) // 30
            days = (days_left % 365) % 30

            print("Manufacturing Date :", self.mfg_date.strftime("%d-%m-%Y"))
            print("Expiry Date        :", self.exp_date.strftime("%d-%m-%Y"))
            print("Time left for expiry:")
            print(years, "Years", months, "Months", days, "Days")


# Input
mfg = input("Enter Manufacturing Date (dd-mm-yyyy): ")
exp = input("Enter Expiry Date (dd-mm-yyyy): ")

# Object creation
p1 = Product(mfg, exp)

# Method call
p1.expiry_details()


