# This file is part of the Python study exercises of a Udemy Course
# 100 Days of Code : The Complete Python Pro Bootcamp

# Day 1 : Beginner - Working with Variables in Python to Manage Data
# print("Hello world!")
# print("Hello world!")
# print("Hello world!")
# print("Hello world!\nHello world!\nHello world!")
# print("Hello" + "Angela")
# print("Hello" + " " + "Angela")
# input("What is your name?")
# print("Hello " + input("What is your name?"))
# print("Hello " + input("What is your name?") + "!")
# You can write it as much as you want, but it won't be excuted as long as you put the '#' in front of the line.
# This line of code will take in input using the input() function.
# name = input("What is your name?")
# print(name)
# name = "Jack"
# print(name)
# name= "Angela"
# print(name)
# print(len(name))
# print(len(input("What is your name?")))
# username =input("What is your name?")
# length =len(username)
# print(length)
# n= "Angela"
# l = len(n)
# print(l)
# user_name_of_this_person = "Angela"
# l = len(user_name_of_this_person)
# print(l)
# nama = "Angela"
# length = len(nama)
# print(length)
# print("Welcome to the Band Name Generator.")
# city = input("What''s the name of the city you grew up in?\n")
# print(city)
# pet = input("What's your pet's name?\n")
# print(pet)
# print("Your band name could be: " + city + " " +  pet)
# print("Welcome to the Band Name Generator.")
# City = input("What's the name of the city you grew up in?\n")
# Pet = input("What's your pet's name?\n")
# print("Your band name could be: " + City + " " + Pet)

# Day 2 : Beginner - Understanding Data Types and How to Manipulate Strings
# print(len(123456))
# above code will give an error beause len() function only works with strings, lists, tuples, etc.
# Subscripting
# print("Hello"[0])
# programming language always starts with 0 index
# # print("Hello"[4])
# print("Hello"[-1])
# print("Hello"[-2])
# # if one is a minus, the program counts going backwards from the end of the string
# String
# print("123" + "456")
# # Integer = Whole number
# print(123 + 345)
# # Large Integers
# print(123_456_789)
# #Float = Decimal number (Floating point nunber)
# print(3.14159)
# #Boolkean = True or False
# print(True)
# print(False)
# len(12345) -> which will be false because 12345 is an integer, not a string.
# #The length function only works with strings, lists, tuples, etc.
# print(len("Hello"))
# print(type("Hello"))
# print(type("abc"))
# print(type(123))
# print(type(3.14159))
# print(type(True))
# print("123" + "456")
# int("123")
# print(int("123") + int("456"))
# print(int("abc")) # This will give a valueerror because "abc" cannot be converted into an integer.
# int()
# float()
# str()
# bool()
# Above code will covert the value into the respective data type.

# name_of_the_user = input("Enter your name\n")
# length_of_name = len(name_of_the_user)
# print(type("Number of letters in your name: ")) #Str
# print(type(length_of_name)) #int
# print("Number of letters in your name: " + str(length_of_name))

# print("My age : " + str(12))
# print(123 + 456)
# print(7 + 3)
# print(3 * 2)
# print(6 / 3)
# print(type(6 / 3))
# print(type(5 / 3))
# print(type(6 // 3))
# print(6 / 3)
# print(5 / 3)
# print(5 // 3)
# print(2 ** 3)

#pendmas
# ()
# **
# *
# /
# +
# -
# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi)) #Coverting float to int
# print(round(bmi)) #Rounding the float to the nearest integer

# print(round(bmi, 2)) #Rounding the float to 2 decimal places

# score = 0
# # User scores a point
# #score = score + 1
# score += 1 # This is a shorthand for score = score + 1
# print(score)
# # score -= 1 # This is a shorthand for score = score - 1

# # # f-strings
# # print("Your score is " + str(score))

# score = 0
# height = 1.8
# is_winning  = True

# print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}.")

# # Day 2 final project
# # print(150 * 1.12 / 5)
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# # bill_with_tip = tip / 100 * bill + bill
# # or
# # bill_with_tip = bill * (1 + tip / 100)
# # or
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# bill_with_tip = bill + total_tip_amount
# bill_per_person = bill_with_tip / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")

# # Day 3 : Beginner - Control Flow and Logical Operators

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# # if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# if height == 120:
#     print("You can ride the rollercoaster!")
# else:
# #     print("Sorry, you have to grow taller before you can ride.")

# if height != 120:
#     print("You can ride the rollercoaster!")
# # else:
# #     print("Sorry, you have to grow taller before you can ride.")


# number_to_check = int(input("What is the number you want to check? \n"))
# # print(number_to_check % 2) 
# if number_to_check % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     elif age <= 22:
#         print("Please pay $10.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y for Yes, N for No: ")
#     if wants_photo == "Y":
#         # Add $3 to their bill for the photo
#         bill += 3
    
#     print(f"Your final bill is: ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# Pizza Order Exercise
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni? Y or N: ")
# # extra cheese = input("Do you want extra cheese? Y or N: ")

# todo : work out how much they need to pay based on their size choice.
# todo : work out how much to add to their bill based on their pepperoni choice.
# todo : work out how much to add to their bill if they want extra cheese.

# <My own solution>--------------------------------------
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# bill = 0

# if size == "S":
#     bill = 15
#     print("Small pizza costs $15.")
# elif size == "M":
#     bill = 20
#     print("Medium pizza costs $20.")
# elif size == "L":
#     bill = 25
#     print("Large pizza costs $25.")

# wants_pepperoni = input("Do you want pepperoni? Y or N: ")
# if wants_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#         print("Small pizza with pepperoni costs $2 extra.")
#     else:
#         bill += 3
#         print("Medium or Large pizza with pepperoni costs $3 extra.")
# wants_extra_cheese = input("Do you want extra cheese? Y or N: ")
# if wants_extra_cheese == "Y":
#     bill += 1
#     print("Extra cheese costs $1 extra.")
# print(f"Your final bill is: ${bill}")
# --------------------------------------------------
# <Instructor's solution>

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0
# if size =="S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs.")
#  # else option also works here because there are only 3 options for size.

# # todo : work out how much to add to their bill based on their pepperoni choice.
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# # todo : work out how much to add to their bill if they want extra cheese.
# if extra_cheese == "Y":
#     bill += 1
# print(f"Your final bill is ${bill}")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55: #or you can write it as 45 <= age <= 55
#         print("Everything is going to be ok. Have a free ride on us!")
#         # No bill for this age group -> we don't need to modify the bill variable because we know that once this condition is met, the bill will remain 0. And it will skip this whole if block and move on.
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you want a photo taken? Y for Yes, N for No: ")
#     if wants_photo == "Y":
#         # Add $3 to their bill for the photo
#         bill += 3
    
#     print(f"Your final bill is: ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# # Day 3 final project(Treasure Island)

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/______/
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a crossroad. Where do you want to go? ' \
# 'Type "left" or "right".\n').lower()
#  # Using .lower() to make the input case-insensitive.
#  # when you put \ before the ' it will not be treated as a string and will be treated as a character.

# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. ' \
#     'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input('You arrive at the island unharmed. There is house with 3 doors. ' \
#                         'One "red", one "yellow", and one "blue". Which color do you choose?\n').lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")

#     else :
#         print("You got attacked by a trout. Game Over.")

# # <Format 1>
# else :
#     print("You fell into a hole. Game Over.")

# #<Format 2>
# # if choice1 == "right":
# #     print("You fell into a hole. Game Over.")

# #If you want to countinue the game, you'll use the first format rather than the second one.

# -----------end of Day 3 final project---------------------


# Day 4 : Beginner - Randomisation and Python Lists------------------------------------------------

# import random
# # random_integer = random.randint(1, 10) # This will give a random integer between 1 and 10 (inclusive)
# # random.randint(a, b) : Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
# random_integer = random.randint(1, 10)
# print(random_integer)

# my_favorite_number = 3.1415

# ------------------------------------
# import random
# import my_module0621
# random_integer = random.randint(1, 10)
# print(random_integer)
# print(my_module0621.my_favorite_number)

# import random
# random_number_0_to_1 = random.random() 
# #random() returns a random float number between 0.0 to 1.0
# print(random_number_0_to_1)
# # This will give a random float number between 0 to 1

# import random
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# import random
# random_float = random.uniform(1, 10)
# # random.uniform(a, b) : Return a random floating point number N such that a <= N <= b for a <= b or b <= N <= a for b < a.
# print(random_float)

# import random
# random_heads_or_tails = random.randint(0, 1)
# if random_heads_or_tails == 0:
#     print("Heads") 
# else:  
#     print("Tails")

# states_of_america = ["Delaware", "Pennsylvania", "Ndw Jersey", "Georgia", "Connecticut", "Massachusetts"]
# print(states_of_america[0]) 
# print(states_of_america[1])
# print(states_of_america[2])
# print(states_of_america[-1]) # This will give the last element of the list
# print(states_of_america[-2]) # This will give the second last element of the list

# states_of_america[1] = "Pencilvania" # This will change the value to the second element of the list

# states_of_america.append("Angelaland") # This will add a new element to the end of the list

# states_of_america.extend(["Hyunland", "Jack Bauer Land"]) # This will add multiple elements to the end of the list

# print(states_of_america) # This will give the updated value of the list

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# # option #1
# print(random.choice(friends))

# # option #2
# random_index = random.randint(0, 4)
# print(friends[random_index])


# states_of_america = ["Delaware", "Pennsylvania", "Ndw Jersey", "Georgia", "Connecticut", "Massachusetts"]

# print(len(states_of_america)) # This will give the length of the list

# num_of_states = len(states_of_america)


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables] # This will create a list of lists
# print(dirty_dozen)
# print(dirty_dozen[1][1]) # This will give the second element of the second list in the list of lists
# print(dirty_dozen[0][2]) # This will give the third element of the first list in the list of lists

# ---------Day 4 Proejct : Rock Paper Scissors------------------

# import random

# rock = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """

# paper ="""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# scissors ="""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """

# game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Tyoe 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 0 and user_choice <= 2:
#     print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose")
# print(game_images[computer_choice])

#option 1 (Angela's Solution)

# if user_choice >= 3 or user_choice <0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif user_choice > computer_choice:
#     print("You win!")
# elif user_choice == 2 and computer_choice == 0:
#     print("You lose!")
# elif computer_choice > user_choice:
#     print("You lose!")
# elif computer_choice == user_choice:
#     print("It's a draw!")

#option 2 (ChatGPT's solution)

# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number. You lose!")
# elif user_choice == computer_choice:
#     print("It's a draw!")
# elif (user_choice == 0 and computer_choice == 2) or \
#      (user_choice == 1 and computer_choice == 0) or \
#      (user_choice == 2 and computer_choice == 1):
#     print("You win!")
# else:
#     print("You lose!")

# ----end of Day 4 Project---------------

# Day 5 : Beginner - Python Loops---------------------------------------------------

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruits)
# print(fruits)


# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

# total_exam_score = sum(student_scores)
# sum = 0
# for score in student_scores:
#     sum += score
# print(sum)


# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


# max_score = 0

# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)

## It's really important to understand the for - in loop function.

# Range function

# for number in range(1, 11, 3):
#     print(number)
# "3" means 1 + 3 + 3 + 3...

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# --------day 5 project : create a Password Generator----------------

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

## Easy level : Generate the password in sequence. Letters, then symbols, then numbers.
# password = ""

# <option 1>
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_letters + 1):
#     password += random.choice(numbers)

# print(password)

# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(symbols)

# for char in range(0, nr_letters):
#     password += random.choice(numbers)

# print(password)

# <Both of the options have the same outcome>

## Hard level : doesn't follow a pattern.
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


# password_list = []
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))

# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))

# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char

# print(f"Your password is {password}")

# ----end of Day 5 Project---------------

# Day 6 : Beginner - Python Functions & Karel ---------------------------------------------------------------------

# print("Hello")
# num_char = len("Hello")
# print(num_char)

# def my_function():
#     print("Hello")
#     print("Bye")

# my_function()

# <Example of how it works>
# def my_function()
#     #Do this
#     #Then do this
#     #Finally do this

# my_function()
    # -> This is called as the "calling function"

# My solution on Reeborg's world-----------------------------
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def one_cycle():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# one_cycle()
# one_cycle()
# one_cycle()
# one_cycle()
# one_cycle()
# one_cycle()

# <no errors found>

# <Angela's solution in Reeborg's world>-----------------------------------
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# for step in range(6):
#     jump()

# ------------------------------
# While loop
# while something_is_true
    #Do this
    #Then do this
    #Then do this
    #until it becomes false

# <Example in reeborg's world>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

    
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# <Hurdle 2 problem solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

    
# while at_goal() != True:
#     jump()

# or

# while not at_goal():
#     jump()

# <Hurdle 3 problem solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# <Hurdle 3 problem>
# <My own solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()
    
## OMG NAILED IT ON ONE GO GET WRECKED ##
# Angela's solution is absolutely the same #

# --------day 6 project : Reeborg's world - Escaping the MAZE ----------------

# <My solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if front_is_clear():
#         move()
#     elif front_is_clear and right_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front and right_is_clear():
#         turn_right()
#         move()
#     else:
#         turn_left()

#.. it has a 50/50 chance of succeeding to its destination. lol

# <Angela's solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

## The above solution is not perfect though, make sure to return after completing day 15.(Debugging purposes)

# ----end of Day 6 Project---------------

# Day 7 : Beginner - Hangman ---------------------------------------------------------------------
# <Step 1>
# import random
# word_list = ["aardvark", "baboon", "camel"]

# ### todo-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# chosen_word = random.choice(word_list)
# print(chosen_word)

# ### todo-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("Guess a letter : ").lower()
# print(guess)

# ### todo-3 Check if the letter the user guessed (guess) is one of letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else :
#         print("Wrong")

# <Step 2>
# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)

# ### todo-1 Create a "placeholder" with the same number of blanks as the chosen_word.
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# guess = input("Guess a letter : ").lower()

# ### todo-2 Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

# display = ""

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)


# # <Step 3>
# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)


# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# ### todo-1 Use a while loop to let the user guess again.

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter : ").lower()

#     display = ""

# ### todo-2 Change the for loop so that you keep the previous correct letters in display.


#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win.")



# # <Step 4>
# import random
# word_list = ["aardvark", "baboon", "camel"]

# chosen_word = random.choice(word_list)
# print(chosen_word)


# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []

# while not game_over:
#     guess = input("Guess a letter : ").lower()

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win.")

# <Due to my own lack of understanding, I need to try it again this time later on this problem.>

# <retry step 1>

# word_list = ["aardvark", "babboon", "camel"]

# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# guess = input("Guess a letter: ").lower()
# print(guess)

# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# <retry step 2>

# word_list = ["aardvark", "babboon", "camel"]

# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# guess = input("Guess a letter: ").lower()


# display = ""

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"
    

# print(display)

# <retry step 3>

# word_list = ["aardvark", "babboon", "camel"]

# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []


# while not game_over:
#     guess = input("Guess a letter: ").lower()


#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
    

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win.")
    
# <retry step 4>



# word_list = ["aardvark", "babboon", "camel"]
# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']


# lives = 6

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# game_over = False
# correct_letters = []


# while not game_over:
#     guess = input("Guess a letter: ").lower()


#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
    

#     print(display)

#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("You lose.")

#     if "_" not in display:
#         game_over = True
#         print("You win.")
    
#     print(stages[lives])


# <step 5 finale>



# import random

# from hangman_words import word_list
# from hangman_art import stages, logo

# lives = 6

# print(logo)

# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print("word to guess: " + placeholder)

# game_over = False
# correct_letters = []


# while not game_over:
#     print(f"*************************************{lives}/6 LIVES LEFT********************************************")
#     guess = input("Guess a letter: ").lower()

#     if guess in correct_letters:
#         print(f"You have already guessed the letter '{guess}'. Try again.")

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(guess)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
    

#     print("Word to guess: " + display)


#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed{guess}, that's not in the word. You lose a life.")


#         if lives == 0:
#             game_over = True


#             print(f"************************IT WAS {chosen_word}!YOU LOSE*****************************")

#     if "_" not in display:
#         game_over = True
#         print("***********************************YOU WIN**********************************")

    
#     print(stages[lives])


# ----end of Day 7 Project--------------

# Day 8 : Beginner - Functions with Outputs -----------------------------------------------------

# def my_function():
#     #Do this
#     #Then do this
#     #Finally do this

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice?")

# greet()


# Functions that allows for inputs

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Angela")

# Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Angela", "London")
# greet_with("Hyun", "Seoul")

# greet_with("Nowhere", "Jack Bauer")
# # The first argument is always the first parameter, and the second argument is always the second parameter.
# # You can also use keyword arguments to sepcify which argument goes to which parameter.

# greet_with(location="Nowhere", name="Jack Bauer")
# # This way you can change the order of the arguments without changing the order of the parameters.


# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with(location="London", name="Angela")
# # This will print the same output as the previous example(like the example above)
# greet_with(location="Seoul", name="Hyun")

# # Day 8 final project(Caesar Cipher)
# Caesar Cipher is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down or up the alphabet.

# TODO-1 : Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
# TODO-2 : Inside the encrypt() function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.
# TODO-3 : Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.
# TODO-4 : What happens if you try to shift z forwards by 9? Can you fix the code?
# TODO-5 : Return the encrypted text


# """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 
#            88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88                                            
# """

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# --------------"Angela's Solution"-------------------------------------------
## <#1 How to encode>
# TODO-1 : Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.

# def encrypt(original_text, shift_amount):

# TODO-2 : Inside the encrypt() function, shift each letter of the 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.


# def encrypt(original_text, shift_amount):
#     cipher_text = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         cipher_text += alphabet[shifted_position]

# print(f"Here is the encoded result: {cipher_text}")

# TODO-3 : Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""



#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the encoded result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)


# TODO-4 : What happens if you try to shift z forwards by 9? Can you fix the code?

# def encrypt(original_text, shift_amount):
#     cipher_text = ""


#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount

#         shifted_position %= len(alphabet) #0~25 withinrange
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the encoded result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)

# <#2 How to decode>------------------

# TODO-1 : Create a function called decrypt() that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2 : Inside the decrypt() function, shift each letter of the 'original_text' backwards in the alphabet by the shift amount and print the decrypted text.

# TODO-3 : Combine the 'encrypt()' and 'decrypt()' functions into a single function called caesar().
         # Use the value of the user chosen direction variable to determine which functionality to use.
         # Call the ceasar() function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

# """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 
#            88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88                                            
# """

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) #0~25 withinrange
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

# encrypt(original_text=text, shift_amount=shift)

# # TODO-1 : Create a function called decrypt() that takes 'original_text' and 'shift_amount' as 2 inputs.
# # TODO-2 : Inside the decrypt() function, shift each letter of the 'original_text' backwards in the alphabet by the shift amount and print the decrypted text.

# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet) #0~25 withinrange
#         output_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {output_text}")

# decrypt(original_text=text, shift_amount=shift)

# # TODO-3 : Combine the 'encrypt()' and 'decrypt()' functions into a single function called caesar().
#          # Use the value of the user chosen direction variable to determine which functionality to use.
#          # Call the ceasar() function instead of encrypt/decrypt and pass in all three variables direction/text/shift.

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:

#         if encode_or_decode == "decode":
#             shift_amount *= -1 # If the user chooses to decode, we need to reverse the shift amount.

#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) #0~25 withinrange
#         output_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {output_text}")

# <current resized code>----------------------------------------------------------

# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 
#            88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88                                            
# """

# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:

#         if encode_or_decode == "decode":
#             shift_amount *= -1 # If the user chooses to decode, we need to reverse the shift amount.

#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) #0~25 withinrange
#         output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")

# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# <#3 Reorganising our code>------------------------------------------------------

# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88 
#            88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88                                            
# """
# # TODO-1 : Print the logo(easy! :3)

# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# # TODO-2 : What happens if the user enters a number/symbol/space?

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode == "decode":
#         shift_amount *= -1 # If the user chooses to decode, we need to reverse the shift amount.
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet) #0~25 withinrange
#             output_text += alphabet[shifted_position]
#     print(f"Here is the {encode_or_decode}d result: {output_text}")


# # TODO-3 : Can you figure out a way to restart the cipher program?

# should_continue = True

# while should_continue:

#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye!")


# ----end of Day 8 Project--------------

# Day 9 : Beginner - Dictionaries, Nesting and the Secret Auction -----------------------------------------------------

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])

# programming_dictionary["Loop"] = "The action of doing something repeatedly."

# # print(programming_dictionary)

# empty_dictionary = {}

# # Wipe and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."

# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }


# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# #print lille out of the travel_log
# print(travel_log["France"][1])  # Output : Lille

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])  # Output : D


# travel_log = {
#     "France": {
#         "cities_visited" : ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# }
# print(travel_log["Germany"]["cities_visited"][2]) # Output : Stuttgart

# Day 9 Project : Secret Auction Program------------------------------------

# print("\n" * 100) # Purpose is to clear the console(screen)

# logo ='''
#    ___________
#    \         /
#     )_______(
#     |"""""""|_.-._,.---------.,_.-._
#     |       | | |               | | ''-.
#     |       |_| |_             _| |_..-'
#     |_______| '-' `'---------'` '-'
#     )"""""""(
#    /_________\
#   /`'-------'`\
#  .-------------.
# /_______________\
# '''
# print(logo)


# # TODO-1 : Ask the user for input

# name = input("What is your name?: ").lower()
# price = int(input("What is your bid?: $"))
# bids = {} # Dictionary to hold bids

# # TODO-2 : Save data into dictionary {name: price}
# bids[name] = price

# # TODO-3 : Whether if new bids need to be added
# should_continue = input("Are there any other bidders Type 'yes' or 'no'. \n").lower()

# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ").lower()
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders Type 'yes' or 'no'. \n").lower()

# As a result the current code goes like this;
# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ").lower()
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders Type 'yes' or 'no'. \n").lower()
#     if should_continue == "no":
#         continue_bidding = False

# # TODO-4 : Compare bids in dictionary
# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder

#     print(f"The winner is {winner} with a bid of ${highest_bid}.")

# # There's a different solution - using the Python max function.
# # <example>
# fruits = {"apple" : 2, "pear" : 4, "orange" : 9}
# max(fruits, key=fruits.get)
# ## max(stats, key=stats.get) <- this will return the key of the highest value.

# As a result the current code goes like this;
# We need to declare the function first before we use it, so it goes like this as the final code;

# logo ='''
#    ___________
#    \         /
#     )_______(
#     |"""""""|_.-._,.---------.,_.-._
#     |       | | |               | | ''-.
#     |       |_| |_             _| |_..-'
#     |_______| '-' `'---------'` '-'
#     )"""""""(
#    /_________\
#   /`'-------'`\
#  .-------------.
# /_______________\
# '''
# print(logo)

# def find_highest_bidder(bidding_dictionary):
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder

#     print(f"The winner is {winner} with a bid of ${highest_bid}.")

# bids = {}
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ").lower()
#     price = int(input("What is your bid?: $"))
#     bids[name] = price
#     should_continue = input("Are there any other bidders Type 'yes' or 'no'. \n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 20)


# ----end of Day 9 Project--------------


### Review purposes
# print("Hello_world")
# print("Hello" + " " + "Angela")

# # Coding exercise #1 - Printing practice
# print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
# print("2. Knead the dough for 10 minutes.")
# print("3. Add 3g of Salt.")
# print("4. Leave to rise for 2 hours.")
# print("5. Bake at 200 degrees C for 30 minutes.")

# # Coding exercise #2 - Debugging practice
# print("Notes from Day 1")
# print("The print statement is used to output strings")
# print("Strings are strings of characters")
# print("String Concatenation is done with the + sign")
# print(("New lines can be created with a \ and the letter n"))

# # Coding exercise #3 - Variables practice
# glass1 = "milk"
# glass2 = "juice"
# temp = glass1
# glass1 = glass2
# glass2 = temp

# # Day 1 Project - Band Name Generator
# print("Welcome to the Band Name Generator.")
# city = input("Which city did you grow up in?\n")
# pet = input("What is the name of your pet?\n")
# print("Your band name could be " + city + " " + pet)

# # Coding exercise #4 - Data Types
# height = 1.65 
# weight = 84

# bmi = weight / height ** 2 # **는 몇 제곱 또는 몇 승

# print(bmi)

# # Day 2 Project - Tip Calculator
# print("Welcome to the tip calculator.")
# bill = float(input("What was the total bill? \n$"))
# tip = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
# people = int(input("How many people to split the bill? \n"))
# # bill_with_tip = bill * (1 + tip / 100)
# # print(bill_with_tip)
# ## 또는
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay ${(final_amount)}")

# 파이썬 f-string은 문자열 앞에 'f'나 'F'를 붙이고, 변수나 표현식을 `{} ` 안에 넣어 문자열에 삽입할 수 있는 방법입니다. 변수뿐만 아니라 간단한 연산, 자릿수 지정, 정렬 기능까지 중괄호 안에서 사용할 수 있어 매우 직관적이고 편리하며, 파이썬 3.6 버전부터 지원하는 주요 문자열 포맷팅 방식입니다. 
# 기본 사용법 
# 문자열 리터럴 앞에 f 또는 F를 붙입니다.
# 삽입하려는 변수나 표현식을 중괄호 {} 안에 넣습니다.
# 예시 변수 삽입.
# Python

#     name = "홍길동"
#     age = 30
#     print(f"안녕하세요, 제 이름은 {name}이고 나이는 {age}세입니다.")
#     # 출력: 안녕하세요, 제 이름은 홍길동이고 나이는 30세입니다.
# 표현식 삽입 (연산).
# Python

#     a = 5
#     b = 10
#     print(f"{a} + {b}는 {a + b}입니다.")
#     # 출력: 5 + 10는 15입니다.
# 추가 기능 소수점 자릿수 지정.
# Python

#     pi = 3.14159265
#     print(f"파이값은 소수점 둘째 자리까지 표현하면 {pi:.2f}입니다.")
#     # 출력: 파이값은 소수점 둘째 자리까지 표현하면 3.14입니다.
# 정렬 기능:
# >: 오른쪽 정렬, <: 왼쪽 정렬, ^: 가운데 정렬 
# Python

#     text = "Hello"
#     print(f"|{text:^10}|") # 가운데 정렬, 총 10자리
#     # 출력: |  Hello   |
# f-string을 사용하는 이유
# 가독성 및 편리성: 다른 포맷팅 방식보다 문법이 직관적이고 코드를 읽기 쉽습니다. 
# 성능: 기존 문자열 포매팅(str.format() 등)보다 속도가 더 빠릅니다. 
# 오류 감소: 변수나 표현식을 문자열 안에 직접 삽입하므로, 타입 오류 등 발생할 수 있는 오류가 줄어듭니다. 

# # Coding exercise #5 - Bmi Calculator with interpretations
# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# # 🚨 Do not modify the values above
# # Write your code below 👇

# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("normal weight")
# elif bmi >= 25:
#     print("overweight")
# else:
#     print("obese")

# # Pizza Order Practice
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want/ S, M, or L? \n")
# pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")

# Small pizza : $15
# Medium pizza : $20
# Large pizza : $25
# Pepperoni for Small pizza : +$2
# Pepperoni for Medium or Large pizza : +$3
# Extra cheese for any size pizza : + $1

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs. Please enter the right size.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# # Lemmie try it again
# # Pizza Order Practice
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want/ S, M, or L? \n")
# pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")

# Small pizza : $15
# Medium pizza : $20
# Large pizza : $25
# Pepperoni for Small pizza : +$2
# Pepperoni for Medium or Large pizza : +$3
# Extra cheese for any size pizza : + $1

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs. Please enter the right size.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# # Review
# # Pizza Order Practice
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L \n")
# pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")

# Small pizza : $15
# Medium pizza : $20
# Large pizza : $25
# Pepperoni for Small pizza : +$2
# Pepperoni for Medium or Large pizza : +$3
# Extra cheese for any size pizza : + $1

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs. Please enter the right size.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# # Day 3 Project - Treasure Island
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
#     if choice2 == "wait":
#         choice3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n').lower()
#         if choice3 == "red": # choice3 cozy
#             print("It's a room full of fire. 불타오르네. Game Over.")
#         elif choice3 == "yellow":
#             print("You found the treasure! You Win, but at what cost?")
#         elif choice3 == "Blue": # choice3 fail
#             print("You enter a room of normies. You die out from awkwardness amongst them. Game Over.")
#         else: # choice3 skill issue
#             print("You're colorblind, you don't read colors. You just open them all up for them to swallow you whole. Game Over.")
#     elif choice2 == "Swim": # choice2 drown?
#         print("You swim with the fishies. Game Over.")
#     else:
#         print("You start to question your life choices, thus further decreasing your sanity. You wait long enough for jesus to take your life. Game Over.")
# elif choice1 == "right": # choice1 fail
#     print("You fell into a hole. Game Over.")
# else: # choice1 YEET
#     print("You don't read English. You YEETED yourself over the cliff. Game Over.")
# ----end of Day 3 Project--------------
# Review on the pizza problem

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: \n")
# pepperoni = input("Do you want pepperoni? Y or N \n")
# extra_cheese = input("Do you want extra cheese? Y or N \n")


# Small pizza : $15
# Medium pizza : $20
# Large pizza : $25
# Pepperoni for Small pizza : +$2
# Pepperoni for Medium or Large pizza : +$3
# Extra cheese for any size pizza : + $1

# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs. Please enter the right size.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")
# -------review complete-------
# Roller coaster problem
# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the roller coaster!")
#     bill = 0
#     age = int(input("What is your age? "))
#     if age <= 12 and age >= 6:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     elif age > 18 and age < 45:
#         bill = 12
#         print("Adult tickets are $12.")
#     else:
#         print("You're either too old or too young lol.")

#     wants_photo = input("Do you want a photo taken? Y or N. \n")
#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is ${bill}.")

# else:
#     print("Too high for ya, skill issue.")


