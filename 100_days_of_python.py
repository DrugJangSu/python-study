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

## RANDOM REVIEW SECTION
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

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# print(states_of_america[1])
# print(states_of_america[-1])
# # states_of_america[1] = "Pencilvania"
# # print(states_of_america[1])
# print(len(states_of_america))
# print(states_of_america)
# # # append is used to add items to the end of the list
# # states_of_america.append("Seoul")
# # print(states_of_america)
# # print(len(states_of_america))

# # extend is used to add multiple items to the end of the list
# states_of_america.extend(["Busan", "Incheon", "Daegu"])
# print(states_of_america)
# print(len(states_of_america))

# import random
# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]


# # option 1
# print(random.choice(friends))

# # option 2
# random_index = random.randint(0, 4)
# print(friends[random_index])


# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # print(states_of_america[49])
# # print(states_of_america[50]) # IndexError: list index out of range(since it doesn't exist)

# num_of_states = len(states_of_america) #50
# print(states_of_america[num_of_states - 1]) #49


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)
# print(dirty_dozen[1][2]) # list in list -> second list, third item
# print(dirty_dozen[1][1]) # list in list -> second list, second item

# <Rock, paper, scissors game review>
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
# import random
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# if user_choice >= 0 and user_choice <=2:
#     print(game_images[user_choice])
# rock = 0
# paper = 1
# scissors = 2
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
# if user_choice >= 3 or user_choice < 0:
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose")
# elif computer_choice > user_choice:
#     print("You lose")
# elif user_choice > computer_choice:
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw")

# <end of rock paper scissors review>

# fruits = ['Apple', 'Peach', 'Pear']
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
#     print(fruits)

# <Quick review - highest score problem>
# student_scores= [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 91, 111, 178, 169, 173, 158, 172, 132, 144, 141, 106, 121, 170, 163, 132, 112, 154, 100, 138, 127, 129, 165, 175, 166, 187, 110, 146, 112, 174, 94, 197, 184, 171, 104, 122, 177, 109, 96, 167]

# total_exam_score = sum(student_scores)
# print(total_exam_score)

# sum = 0
# for score in student_scores:
#     sum += score

# print(sum)

# # how to fnd the highest score
# max = 0
# for score in student_scores:
#     if score > max:
#         max = score

# print(f"The highest score in the class is: {max}")

# Angela's solution

# max_score = 0
# for score in student_scores:
#     if score > max_score:
#         max_score = score
# print(max_score)

# <end of highest score review>

# Range Fuction with For loop

# for number in range(1, 10): # 1 to 9, not including 10
#     print(number)
# for number in range(1, 11): # 1 to 10
#     print(number)
# for number in range(1, 11, 3): # 1 to 10, increasing by 3
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number # total = total+number
# print(total)

# # <FIZZBUZZ GAME>
# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

# Your program should print each number from 1 to 100 in turn and include number 100.

# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# e.g. it might start off like this:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ...etc

# # <My solution>
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# # <Angela's solution>
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# <end of FIZZBUZZ review>
# <Quick review - Pypassword Generator>

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# import random

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE
# password = ""
# for char in range(1, nr_letters + 1): #char is for character(dummy variable)
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# Hard Level - Order of characters randomised:
# password_list = []
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))
# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))

# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")

# <Hard level review>
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# import random

# password_list = []
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))
# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))

# random.shuffle(password_list)

# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")

# <end of Pypassword Generator review>

# print("Hello")
# num_char = len("Hello")
# print(num_char)

# def my_function():
#     print("Hello")
#     print("Bye")
#     print("See you later")

# my_function() #this is how to execute the defined function, without any print statement

# <Reeborg's world review>
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


# for step in range(0, 6):
#     jump()

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

# <hurdle1>
# number_of_hurdles = 6
# while number_of_hurdles >0:
#     jump()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# <hurdle2>
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

# while not at_goal():
#     jump()

# #<hurdle3> # Position of the hurdle and the numbers are random
# # <My solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():    # I got rid of the "move" in the first line due to not knowing where the hurdle is
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     elif wall_in_front():
#         jump()

# <hurdle4> # Position of the hurdle and the numbers are random, and the height of the hurdle is also random
# <my solution>
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while not wall_in_front():
#         move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# <Final project review : Maze>
# <My solution>

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while not at_goal():
#     if front_is_clear() and wall_on_right():
#         move()
#     elif front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front() and wall_on_right():
#         turn_left()
#     elif wall_in_front and right_is_clear():
#         turn_right()
#         move()

## Success without any errors! Happy Hyun noises----------------
# No debugging required for my solution

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

# However, this solution doesn't work in some cases, for example, when there's a long straight path with no turns. In such cases, the robot may not reach the goal because it only turns right when the right side is clear. If the robot encounters a situation where it needs to turn left to reach the goal, it won't do so because of the current logic.
# To address this, we can modify the logic to include a left turn when both the front and right sides are blocked. Here's an updated version of the code;

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move() 
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# ---------------------------------------------------

# <Hangman exercise review>
# <part 1>
# word_list = ["aardvark", "baboon", "camel"]

# TODO-1 : Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# TODO-2 : Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# TODO-3 : Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if the letter is in the chosen_word. Otherwise, print "Wrong".

# <My solution>
# # TODO-1 
# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO-2
# guess = input("Guess a letter: ").lower()

# # TODO-3
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

# <Angela's solution>
# # # TODO-1 
# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# # # TODO-2
# guess = input("Guess a letter: ").lower()
# print(guess)

# # # TODO-3
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
# ---------------------------------------------------
# <part 2>


# TODO-1 : Create a "placeholder" with the same number of letters as the chosen_word and assign it to a variable called display. For example, if the chosen_word has 6 letters, display should be ["_", "_", "_", "_", "_", "_"].
# TODO-2 : Create a "display" that puts the guess letter in the correct position(s). For example, if the user guessed "a" and the chosen_word was "apple", then display should be ["a", "_", "_", "a", "_"].
# TODO-3 : Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3. You don't need to worry about the case where the user enters a letter they've already guessed. We'll deal with that in step 3.

# word_list = ["aardvark", "baboon", "camel"]


# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# # TODO-1
# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# guess = input("Guess a letter: ").lower()
# # TODO-2

# display = ""

# for letter in chosen_word:
#     if letter == guess:
#         display += letter
#     else:
#         display += "_"

# print(display)
# ---------------------------------------------------
# <part 3>

# TODO-1 : Yse a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more "_" characters.
# TODO-2 : Change the for loop so that you keep the previous correct guesses in 'display'. For example, if the chosen_word was "apple" and the user guessed "p", then display should be ["_", "p", "p", "_", "_"].

# word_list = ["aardvark", "baboon", "camel"]


# import random
# chosen_word = random.choice(word_list)
# print(chosen_word)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# # TODO-1

# game_over = False
# correct_letters = []


# while not game_over:
#     guess = input("Guess a letter: ").lower()


#     display = ""

#     # TODO-2

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(letter)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print(display)

#     if "_" not in display:
#         game_over = True
#         print("You win!")

# ----------------------------------------------------
# <part 4>

# TODO-1 : Create a variable called 'lives' to keep track of the number of lives left. Set it to 6.
# TODO-2 : If the letter is not in the chosen_word, then reduce 'lives' by 1. If lives goes down to 0 then the game should stop and it should print "You lose."
# TODO-3 : Print the ASCII art from 'stages' at the end of each round, so the user knows how many lives they have left.

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

# word_list = ["aardvark", "baboon", "camel"]

# # TODO-1
# lives = 6

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
#             correct_letters.append(letter)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"
#         # rather tampering with the elif and else statement, just write a completely separate statement so that we can keep our logic separate and under different banners, and easier to read and debug
#     print(display)

#     # TODO-2
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             game_over = True
#             print("You lose.")

#     if "_" not in display:
#         game_over = True
#         print("You win!")
    
#     # TODO-3

#     print(stages[lives])

# ----------------------------------------------------
# <part 5>

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

# word_list = ["aardvark", "baboon", "camel"]

# lives = 6

# import random
# chosen_word = random.choice(word_list)

# placeholder = ""
# word_length = len(chosen_word)
# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)


# game_over = False
# correct_letters = []


# while not game_over:
#     print(f"********************<{lives}>/6 LIVES LEFT********************")
#     guess = input("Guess a letter: ").lower()

#     if guess in correct_letters:
#         print(f"You've already guessed {guess}")

#     display = ""

#     for letter in chosen_word:
#         if letter == guess:
#             display += letter
#             correct_letters.append(letter)
#         elif letter in correct_letters:
#             display += letter
#         else:
#             display += "_"

#     print("Word to guess: " + display)

#     if guess not in chosen_word:
#         lives -= 1
#         print(f"You guessed {guess}, that's not in the word. You lose a life.")
#         if lives == 0:
#             game_over = True
#             print(f"*************************IT WAS <{chosen_word}>YOU LOSE*************************")

#     if "_" not in display:
#         game_over = True
#         print("*************************YOU WIN*************************")
    

#     print(stages[lives])

# ----<end of Hangman review>---------------------------

# Functions with inputs

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()

# # example
# def my_function(something):
#     # Do this with something
#     # Then do this
#     # Finally do this

# Functions that allows for inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print(f"Isn't the weather nice today, {name}?")

# greet_with_name("Hyun")

# In this case, name is parameter, and "Hyun" is argument
# The Paramenter is the name of the data that's being passed into the function
# The Argument is the actual value of the data
# You can have multiple parameters

## Coding exercise - Life in weeks

# def life_in_weeks(age):
#     weeks = int((90 - age) * 52)
#     print(f"You have {weeks} weeks left.")


# life_in_weeks(12)

# ------------------------------
# Another solution
# def life_in_weeks(age):
#     if age < 0 or age > 90:
#         print("Please enter a valid age between 0 and 90.")
#         return
    
#     weeks = (90 - age) * 52 
#     print(f"You have {weeks} weeks left.")
#     return weeks  # 필요하면 반환값 제공

# life_in_weeks(12)
# ------------------------------
# Positional arguments vs Keyword arguments

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Hyun", "Seoul") # Positional arguments
# greet_with(location="Seoul", name="Hyun") # Keyword arguments
# # Keyword arguments are more flexible than positional arguments
# # You can also mix positional and keyword arguments, but positional arguments must come first

# ------------------------------
# Coding exercise - Love calculator
# # -----my solution-----
# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()

#     t = combined_names.count("t")
#     r = combined_names.count("r")
#     u = combined_names.count("u")
#     e = combined_names.count("e")

#     true = t + r + u + e

#     l = combined_names.count("l")
#     o = combined_names.count("o")
#     v = combined_names.count("v")
#     e = combined_names.count("e")

#     love = l + o + v + e

#     love_score = int(str(true) + str(love))

#     print(love_score)

# calculate_love_score("Kayne West", "Kim Kardashian")
# calculate_love_score("Jong Hyun Lee", "Thea Lucie Bailey")

# # ----Angela's Solution---
# def calculate_love_score(name1, name2):
#     combined_names = name1 + name2
#     lower_names = combined_names.lower()
    
#     t = lower_names.count("t")
#     r = lower_names.count("r")
#     u = lower_names.count("u")
#     e = lower_names.count("e")
#     first_digit = t + r + u + e
    
#     l = lower_names.count("l")
#     o = lower_names.count("o")
#     v = lower_names.count("v")
#     e = lower_names.count("e")
#     second_digit = l + o + v + e
    
    
#     score = int(str(first_digit) + str(second_digit))
#     print(score)
    
# calculate_love_score("Kanye West", "Kim Kardashian")

# ----------------------------------------------------------
# Day 8 project - Caesar Cipher
# <PART 1>
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
# TODO-1: Create a function called 'encrypt()' that takes the 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'encrypt' function, shift each letter of 'original_text' forwards in the alphabet by the shift amount and print the encrypted text.

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.

# TODO-4: What happens if you try to shift the letter 'z' forwards by 9? Can you fix the code?

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# # TODO-1, TODO-2


# def encrypt(original_text, shift_amount):
#     cipher_text = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount

#         shifted_position %= len(alphabet) #0 to 25
#         cipher_text += alphabet[shifted_position]

#     print(f'Here is the encoded result: {cipher_text}')

# # TODO-3

# encrypt(original_text = text, shift_amount = shift) # Keyword arguments

# <PART 2>-----------------------


# TODO-1: Create a function called 'decrypt()' that takes the 'originai_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'decrypt' function, shift each letter of 'original_text' backwards in the alphabet by the shift amount and print the decrypted text.

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'. This function should take the 'original_text', 'shift_amount', and 'cipher_direction' as inputs.
# Use the value of the user chosen 'direction' variable to determine whether to encrypt or decrypt the message.


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) #0 to 25
#         cipher_text += alphabet[shifted_position]
#     print(f'Here is the encoded result: {cipher_text}')


# # TODO-1, TODO-2
# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet) #0 to 25
#         output_text += alphabet[shifted_position]
#     print(f'Here is the decoded result: {output_text}')

# TODO-3 <Combining encrypt and decrypt function into one function called caesar()>
# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:

#         if encode_or_decode =="decode":
#             shift_amount *= -1

#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) #0 to 25
#         output_text += alphabet[shifted_position]
#     print(f'Here is the {encode_or_decode}d result: {output_text}')


# caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)


## So this is the result of part 2----------------------------

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:

#         if encode_or_decode =="decode":
#             shift_amount *= -1

#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet) #0 to 25
#         output_text += alphabet[shifted_position]
#     print(f'Here is the {encode_or_decode}d result: {output_text}')


# caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)


# <PART 3>-----------------------
# # TODO-1
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
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# # text = input("Type your message:\n").lower()
# # shift = int(input("Type the shift number:\n"))

# # TODO-1: Import and print the logo
# # TODO-2: What happens if the user enters a number/symbol/space?
# # TODO-3: Can you figure out a way to restart the cipher program?

# # TODO-2

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter # It means that if it's not an alphabet, it'll just add it into the result without encode/decoding
#         else:
#             if encode_or_decode =="decode":
#                 shift_amount *= -1

#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet) #0 to 25
#             output_text += alphabet[shifted_position]
#     print(f'Here is the {encode_or_decode}d result: {output_text}')

# # TODO-3

# should_continue = True

# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))

#     caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)

#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye")


#### Hmm. is there a bug in this current bug?
# encode - ab - 2 it would be cd.
# But if we decode - cd - 2 it would be af instead of ab.
# if encode_or_decode =="decode":
# shift_amount *= -1
# -> This is the problem. So we need to take it out of the for loop
# So below is the actual fixed code <FINAL RESULT>

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
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def caesar(original_text, shift_amount, encode_or_decode):
#     output_text = ""
#     if encode_or_decode =="decode":
#         shift_amount *= -1
#     for letter in original_text:
#         if letter not in alphabet:
#             output_text += letter 
#         else:
#             shifted_position = alphabet.index(letter) + shift_amount
#             shifted_position %= len(alphabet) #0 to 25
#             output_text += alphabet[shifted_position]
#     print(f'Here is the {encode_or_decode}d result: {output_text}')

# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     caesar(original_text = text, shift_amount = shift, encode_or_decode = direction)
#     restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
#     if restart == "no":
#         should_continue = False
#         print("Goodbye")


# FIRST SUCCESS # However review is required in the future.
# End of caesar cipher project
# -------end of day 8--------

# < DAY 9 - Dictionaries, Nesting and the Secret Auction>

# Silent auction
# - Where everybody bids silently, and no one knows the other person's bid until at the very end of the auction, where the highest bid is revealed.

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# print(programming_dictionary["Bug"])

# programming_dictionary["Loop"] = "The action of doing something over and over again until a certain condition is met."
# ## This actually adds the new key(item) and value(definition) pair into the dictionary

# print(programming_dictionary)


# empty_dictionary = {}

# ## Wipe an existing dictionary
# # programming_dictionary = {}
# # print(programming_dictionary)

# # Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary["Bug"])

# print(programming_dictionary)

# # Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


## Coding Exercise - Grading Program----------------

# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 

# Write a program that converts their scores to grades.

# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 

# The final version of the student_grades dictionary will be checked. 

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 

# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student, score in student_scores.items():
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

## student_scores.items() -> (이름, 점수) 한 쌍씩 꺼냄
## for student, score in ->	이름과 점수를 각각 변수로 받음
## if / elif / else	-> 점수를 비교해서 등급 정함
## student_grades[student] -> 새 딕셔너리에 등급 저장

# ----------------------------------------------

# ## Nesting and dictionaries
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# # Nested List in a Dictionary;
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }
# #If I want to print Lille
# print(travel_log["France"])
# print(travel_log["France"][1])

# nested_list = ["A", "B", ["C", "D"]]
# #If I want to print D
# print(nested_list[2][1])

# ## This is a list nested inside a dictionary which is nested inside another dictionary.
# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },    
#     "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#     "total_visits": 5
#     },
# }

# # If I want to print out Stuttgart from this travel_log
# print(travel_log["Germany"]["cities_visited"][2])

## The Secret Auction Program Instructions and Flow Chart<SECTION 9 PROJECT>

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
# ## TODO-1 Ask the user for input & print the logo

# ## TODO-2 Save data into dictionary {name: price}

# ## TODO-3 Ask if whether new bids need to be added(any new bidders)

# ## TODO-4 Compare bids in dictionary and find the highest bidder

# print(logo)
# def find_highest_bidder(bidding_dictionary):
#     winner = ""
#     highest_bid = 0
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}.")


# bids = {} # This is an empty dictionary to store the bids
# continue_bidding = True
# while continue_bidding:
#     name = input("What is your name?: ")
#     price = int(input("What is your bid?: $"))
#     bids[name] = price # Storing the name and price into the dictionary
#     should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
#     if should_continue == "no":
#         continue_bidding = False
#         find_highest_bidder(bids)
#     elif should_continue == "yes":
#         print("\n" * 50) # This is to clear the screen for the next bidder
#         print("Cleared the screen for the next bidder.")

## TODO-4 Compare bids in dictionary and find the highest bidder

## Deffo need to review this for later.
# -------------------------------------------------------------------
# End of day 9-------------------------------------------------------

# Day 10 - Functions with Outputs------------------------------------
## Building a calculator app(text based calculator)
## More Functions

# # This is a normal function
# def my_function():
#     result = 3 * 2
#     return result

# # and if I put this function again
# def my_function():
#     return 3 * 2

# # and this is how you call the function
# output = my_function()

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())
    
# format_name(f_name = "angela", l_name = "aNgElA")

## .title() <- This method capitalizes the first letter of each word in a string and makes all other letters lowercase.(첫 문자 대문자)


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     ## Capturing the formatted first name and last name into new variables as "formated_f_name" and "formated_l_name"

#     print(f"{formated_f_name} {formated_l_name}")
    

# format_name(f_name = "anGeLa", l_name = "yU")


## Instead of printing the result out, return the formated name as a single string

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return f"{formated_f_name} {formated_l_name}"
# #This formated string becomes the output of the function, as the output replacest the part where the function was called.

# formated_string = format_name(f_name = "anGeLa", l_name = "yU")
# print(formated_string)

# # Can also d this alternatively y taking the function call directly inside the print statement
# print(format_name(f_name = "anGeLa", l_name = "yU"))


# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output =function_1("hello")
# print(output)

# # what if we take the output of function_1 and pass it into function_2?

# output = function_2(function_1("hello"))
# print(output)

# # This is how the return function works. -> this is the reason why we use return instead of print inside the function.

# 1234567890-=1234567890!@#$%^&*()_+

## Fuctions with Outputs<review>

# def my_function():
#     result = 3 * 2
#     return result
## * In this case the output is he result


## .title() <- This method capitalizes the first letter of each word in a string and makes all other letters lowercase.    formated_f_name = f_name.title()

# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name(f_name = "lee", l_name = "JONG HYUN")


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     print(f"{formated_f_name} {formated_l_name}")

# format_name(f_name = "lEe", l_name = "JONG HYUN")

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# formated_string = format_name(f_name = "lEe", l_name = "JONG HYUN")
# print(formated_string)

# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# print(format_name(f_name = "lEe", l_name = "JONG HYUN"))

## the return keyword allows you to capture the output of a function and use it later in your code.

## The difference between the return function and the print function is that the return function gives back a value that can be used later, while the print function simply displays the value on the screen.

# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_1("hello")
# print(output)

# output = function_2(function_1("hello"))
# print(output)


## Multiple Return Values ##

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}"

# print(format_name(input("What is your first name?"), input("What is your last name?")))

## Coding Exercise 10: Leap Year (윤년)

# 윤년(Leap Year) 판단 규칙
# 어떤 연도가 윤년인지 판단하려면;
# 4로 나누어 떨어지면 윤년이다.
# → 예: 2004, 2024
# 단! 100으로 나누어 떨어지면 윤년이 아니다.
# → 예: 1900, 2100은 윤년 아님
# 하지만!! 400으로 나누어 떨어지면 다시 윤년이다.
# → 예: 1600, 2000은 윤년

# <My Solution>
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_leap_year(2400))
# print(is_leap_year(1989))
# print(is_leap_year(2024))

## --------------------------------------

## Docstrings ##
# Docstrings are basically a way to explain what your function does.

# def format_name(f_name, l_name):
#     """Takes first and last names and format it to return the title case version of the name."""
#     ## This is a docstring that explains what the function does.(three quotation marks)
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"

# formatted_name = format_name("jong hyun", "lee")

# length = len(formatted_name)

# """sdsdsf
# dfdfdfdf
# dfdfdf
# dfdf
# lol
# """
# # sdsddssdf
# # sdfdsfds
# # dsfdsfds

# """ -> this is a doc"""

## Day 10 project - The Calculator Project ##

# TODO-1: Write out the other 3 functions - subtract, multiply and divide

# def add(n1, n2): # 덧셈
#     return n1 + n2

# def multiply(n1, n2): # 뺄셈
#     return n1 * n2

# def subtract(n1, n2): #곱셈
#     return n1 - n2

# def divide(n1, n2): #나눗셈
#     return n1 / n2

# # TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
# operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide,}
# ## Remember not to trigger the functions because we're storing it and not using it, thus we don't use parentheses. This is literally a dictonary that stores functions as values.

# # TODO-3: Use the dictionary ooperations to perform the calculations. (multiply 4 * 8 using the dictonary)

# print(operations["*"](n1 = 4, n2 = 8))

# # <This is the basic structure of the calculator app>

# <Angela's solution>--------------------------------------------

# art_logo = """
#  _____________________
# |  _________________  |
# | | Jong Hyun.      | |  .----------------.  .----------------.  .----------------.  .----------------.
# | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
# |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
# | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
# | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
# | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
# | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
# | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
# | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
# | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
# | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
# |_____________________|
# """

# def add(n1, n2): 
#     return n1 + n2

# def multiply(n1, n2): 
#     return n1 * n2

# def subtract(n1, n2):
#     return n1 - n2

# def divide(n1, n2): 
#     return n1 / n2

# operations = {"+" : add, "-" : subtract, "*" : multiply, "/" : divide,}

# def calculator():
#     print(art_logo)
#     should_accmulate = True
#     num1 = float(input("What is the first number?: "))

#     while should_accmulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Pick an operation: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

#         if choice == 'y':
#             num1 = answer
#         else:
#             should_accmulate = False
#             print("\n" * 20)
#             calculator() # Restarting the calculator function- this is called recursion

# calculator()

# --------------<end of Day 10>------------------------

# Day 11 - The Blackjack Capstone Project------------------------------------

# ## Project Instructions
# In this project, you will be creating a text-based version of the card game Blackjack.
# The rules of the game are as follows:
# Try to get as close to 21 as possible without going over (busting).
# 2 to 9 is face value
# 10, J, Q, K is worth 10
# Ace is worth 11 or 1
# The deck is unlimited in size. There are no jokers. The cards in the deck have equal probability of being drawn.

# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# four 10s represent 10, J, Q, K
# 11 represents Ace, until the number goes above 21 which it becomes 1.

## <Angela's Solution>-----------------------------
## ----<Hint 4 and 5>----

# import random

## Hint 4 : Create a function deal_card() that uses the random module to return a random card from the list of cards.

# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
## Hint 5 : Deal with the user and computer 2 cards each using deal-card() and append().

# user_cards = []
# computer_cards = []

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())


### Current code status ###
# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_cards = []
# computer_cards = []

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

## Hint 6 : Create a function calculate_score() that takes a List of cards as input and returns the score. Use the sum() function to get the score.

# def calculate_score(cards):
#     return sum(cards)

## Hint 7 : Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.


# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0

#     return sum(cards)

## Hint 8 : Inside calculate_score() check for an 11 (ace). If the score is over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

### Current code status ###
# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# user_cards = []
# computer_cards = []
# is_game_over = False

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

## Hint 9 Call the function calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# user_score = calculate_score(user_cards)
# computer_score = calculate_score(computer_cards)
# print(f"Your cards: {user_cards}, current score: {user_score}")
# print(f"Computer's first card: {computer_cards[0]}")


# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True

### Current code status ###
# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# user_cards = []
# computer_cards = []
# is_game_over = False

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# user_score = calculate_score(user_cards)
# computer_score = calculate_score(computer_cards)
# print(f"Your cards: {user_cards}, current score: {user_score}")
# print(f"Computer's first card: {computer_cards[0]}")


# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True

## Hint 10 : If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# else:
#     user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#     if user_should_deal == "y":
#         user_cards.append(deal_card())
#     else:
#         is_game_over = True


### Current code status ###
# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# user_cards = []
# computer_cards = []
# is_game_over = False

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# user_score = calculate_score(user_cards)
# computer_score = calculate_score(computer_cards)
# print(f"Your cards: {user_cards}, current score: {user_score}")
# print(f"Computer's first card: {computer_cards[0]}")


# if user_score == 0 or computer_score == 0 or user_score > 21:
#     is_game_over = True
# else:
#     user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#     if user_should_deal == "y":
#         user_cards.append(deal_card())
#     else:
#         is_game_over = True

## Hint 11 : The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# user_cards = []
# computer_cards = []
# computer_score = -1 # Initializing to a dummy value
# user_score = -1    # Initializing to a dummy value
# is_game_over = False

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# while not is_game_over:
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"Your cards: {user_cards}, current score: {user_score}")
#     print(f"Computer's first card: {computer_cards[0]}")


#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#         if user_should_deal == "y":
#             user_cards.append(deal_card())
#         else:
#             is_game_over = True

## Hint 12 : Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)


### Current code status ###
# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# user_cards = []
# computer_cards = []
# computer_score = -1 # Initializing to a dummy value
# user_score = -1    # Initializing to a dummy value
# is_game_over = False

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# while not is_game_over:
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"Your cards: {user_cards}, current score: {user_score}")
#     print(f"Computer's first card: {computer_cards[0]}")


#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#         if user_should_deal == "y":
#             user_cards.append(deal_card())
#         else:
#             is_game_over = True


# while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

## Hint 13 : Create a function compare() and pass in the user_score and computer_score.

# import random
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "It's a draw!"
#     elif c_score == 0:
#         return "Lose,opponent has a Blackjack!"
#     elif u_score == 0:
#         return "Win with a Blackjack!"
#     elif u_score >21:
#         return "You went over. You lose!"
#     elif c_score >21:
#         return "Opponent went over. You win!"
#     elif u_score > c_score:
#         return "You win!"
#     else:
#         return "You lose!"
    ### In elif functions, the order of the conditions matter.(From top to bottom)

# user_cards = []
# computer_cards = []
# computer_score = -1 
# user_score = -1    
# is_game_over = False

# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())

# while not is_game_over:
#     user_score = calculate_score(user_cards)
#     computer_score = calculate_score(computer_cards)
#     print(f"Your cards: {user_cards}, current score: {user_score}")
#     print(f"Computer's first card: {computer_cards[0]}")


#     if user_score == 0 or computer_score == 0 or user_score > 21:
#         is_game_over = True
#     else:
#         user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#         if user_should_deal == "y":
#             user_cards.append(deal_card())
#         else:
#             is_game_over = True


# while computer_score != 0 and computer_score < 17:
#     computer_cards.append(deal_card())
#     computer_score = calculate_score(computer_cards)

# print(f"Your final hand: {user_cards}, final score: {user_score}")
# print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
# print(compare(user_score, computer_score))

### Current code status ###
# import random
# logo = """
#  _     _            _    _            _    
# | |   | |          | |  (_)          | |   
# | |__ | | __ _  ___| | ___  __ _  ___| | __
# | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# | |_) | | (_| | (__|   <| | (_| | (__|   < 
# |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
#                        _/ |                
#                       |__/      
# """

# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "It's a draw!"
#     elif c_score == 0:
#         return "Lose,opponent has a Blackjack!"
#     elif u_score == 0:
#         return "Win with a Blackjack!"
#     elif u_score >21:
#         return "You went over. You lose!"
#     elif c_score >21:
#         return "Opponent went over. You win!"
#     elif u_score > c_score:
#         return "You win!"
#     else:
#         return "You lose!"
 
# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     computer_score = -1 
#     user_score = -1    
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")


#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True


#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
#     print("\n" * 20)
#     play_game()


# -------Final code---------
# import random

# logo = """
#  _     _            _    _            _    
# | |   | |          | |  (_)          | |   
# | |__ | | __ _  ___| | ___  __ _  ___| | __
# | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# | |_) | | (_| | (__|   <| | (_| | (__|   < 
# |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
#                        _/ |                
#                       |__/      
# """

# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
    
#     if 11 in cards and sum(cards) < 21:
#         cards.remove(11)
#         cards.append(1)
    
#     return sum(cards)

# def compare(u_score, c_score):
#     if u_score == c_score:
#         return "It's a draw!"
#     elif c_score == 0:
#         return "Lose,opponent has a Blackjack!"
#     elif u_score == 0:
#         return "Win with a Blackjack!"
#     elif u_score >21:
#         return "You went over. You lose!"
#     elif c_score >21:
#         return "Opponent went over. You win!"
#     elif u_score > c_score:
#         return "You win!"
#     else:
#         return "You lose!"
 
# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     computer_score = -1 
#     user_score = -1    
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())

#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")


#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True


#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)

#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
#     print("\n" * 20)
#     play_game()

# -------------------<end of Day 11>------------------------

## Day 12 : Scope & Number Guessing Game------------------------------------

## Namespaces : Local vs Global Scope
# Scope : The region that a variable is recognized.(범위)


# <Introduction of scope>
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")    

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# ## In this case, the enemies variable inside the function is a local variable, while the enemies variable outside the function is a global variable.

## Local Scope : When you create a new variable inside a function, that variable is only available inside that function.

# def drink_potion():
#     potion_strength = 2 
#     print(potion_strength) # This will print 2 because potion_strength is defined within the function.

# drink_potion()
# print(potion_strength) # This will give an error because potion_strength is a local variable and cannot be accessed outside the function.



## Global Scope : A variable created in the main body of the code is a global variable and can be used by any function.

# player_health = 10 # This is a global variable

# def drink_potion():
#     potion_strength = 2 # This is a local variable
#     print(player_health) # This will print 10 because player_health is a global variable.

# drink_potion()
# print(player_health) # This will print 10 because player_health is a global variable.

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()

# print(player_health) 

## Does Python has a block scope like other programming languages?

# No, Python does not have block scope. Variables defined inside blocks such as if statements or for loops are still accessible outside of those blocks within the same function or global scope.
# 블록 스코프(block scope)'란 코드의 블록(\(\{\}\)) 안에서 선언된 변수가 해당 블록 안에서만 유효하고, 블록 밖에서는 접근할 수 없는 범위를 의미함.

# if 3 > 2:
#     a_variable = 10

# game_level = 3
# enemies = ["Skeletion", "Zombie", "Alien"]

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy) # This will print "Skeletion" because new_enemy is defined in the global scope.


# game_level = 3
# enemies = ["Skeletion", "Zombie", "Alien"]

# def create_enemy():
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

## If you create a variable inside the function, it's only available inside that function.(local scope)
## If you create a variable outside the function, it's available anywhere in the code.(global scope)


# game_level = 10
# enemies = ["Skeletion", "Zombie", "Alien"]

# def create_enemy():
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)


## Coding exercise 11 : Prime Number Checker

# def is_prime(num):
#     if num == 1:
#         return False
#     if num == 2:
#         return True
    
#     for i in range(2, num):
#         if num % i == 0:
#             return False
    
#     return True

# print(is_prime(73))
# print(is_prime(75))

## --------------------------------------

## How to modify a global variable


# enemies = "Skeletion"

# def increase_enemies():
#     enemies = "Zombie"
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# enemies = 1


# def increase_enemies():
#     global enemies # This line tells Python that we want to use the global variable enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

##  Modifying the global variable isn't much recommended as it can lead to code that is difficult to debug and maintain. It's generally better to return a value from a function and assign it to a variable outside the function. (especially in a function that has a local variable with the same name as the global variable)



# Way that you want to have this functionality like a function that changes the number of enemies without modifying the global variable directly.

# enemies = 1

# def increase_enemies(enemy):
#     print(f"enemies inside function: {enemies}")
#     return enemy + 1

# enemies = increase_enemies(enemies)
# print(f"enemies outside function: {enemies}")

## Python Constants and Global Scope

# Global constants are variables which you define and you're never planning to change it ever again.(상수, 즉 변하지 않는 값)

# PI = 3.14159
# GOOGLE_URL = "https://www.google.com"
# Uppercase variable names are used to indicate that these variables should be treated as constants and not modified.(관례적으로 대문자 사용)

# def my_func():
#     print(PI)
#     print(GOOGLE_URL)

## DAY 12 Final project : The Number Guessing Game ## --------

## Choosing a random number between 1 and 100.
## Function to set difficulty(Easy is 10 attempts, Hard is 5 attempts)
## Let the user guess a number
## Function to check users' guess against actual answer.
## Track the number of turns and reduce by 1 if they get it wrong
## Repeat the guessing functionality if they get it wrong.
# ------------------------------------------------
# from random import randint
# logo = """                                                                                                                                        

#   _  _            _                ___                _              ___                
#  | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
#  | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
#  |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
#                                                             |___/                       
# """

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5


# ## Function to check users' guess against actual answer.
# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns -1
#     else:
#         print(f"You got it! The answer was {actual_answer}")

# # Function to set difficulty
# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS

# def game():
#     print(logo)
#     ## Choosing a random number between 1 and 100.
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(a= 1, b= 100)
#     print(f"Pssst. the correct answer is {answer}")


#     turns = set_difficulty()

#     ## Let the user guess a number
#     ## Repeat the guessing functionality if they get it wrong.
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess= int(input("Make a guess: "))
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses. You lose")
#             return
#         elif guess != answer:
#             print("Guess again.")
#     ## Track the number of turns and reduce by 1 if they get it wrong.

# game()


## <Final code>---------------------------------------------------------------------
# from random import randint
# logo = """                                                                                                                                        

#   _  _            _                ___                _              ___                
#  | \| |_  _ _ __ | |__  ___ _ _   / __|_  _ ___ _____(_)_ _  __ _   / __|__ _ _ __  ___ 
#  | .` | || | '  \| '_ \/ -_) '_| | (_ | || / -_|_-<_-< | ' \/ _` | | (_ / _` | '  \/ -_)
#  |_|\_|\_,_|_|_|_|_.__/\___|_|    \___|\_,_\___/__/__/_|_||_\__, |  \___\__,_|_|_|_\___|
#                                                             |___/                       
# """

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# def check_answer(user_guess, actual_answer, turns):
#     """Checks answer against guess, returns the number of turns remaining."""
#     if user_guess > actual_answer:
#         print("Too high.")
#         return turns - 1
#     elif user_guess < actual_answer:
#         print("Too low.")
#         return turns -1
#     else:
#         print(f"You got it! The answer was {actual_answer}")

# def set_difficulty():
#     level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#     if level == "easy":
#         return EASY_LEVEL_TURNS
#     else:
#         return HARD_LEVEL_TURNS

# def game():
#     print(logo)
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     answer = randint(a= 1, b= 100)
#     print(f"Pssst. the correct answer is {answer}")
#     turns = set_difficulty()
#     guess = 0
#     while guess != answer:
#         print(f"You have {turns} attempts remaining to guess the number.")
#         guess= int(input("Make a guess: "))
#         turns = check_answer(guess, answer, turns)
#         if turns == 0:
#             print("You've run out of guesses. You lose")
#             return
#         elif guess != answer:
#             print("Guess again.")

# game()

# --------------------------End of day 12---------------------------

## Day 13 : Debugging --------------------------------------------------
# example)
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")


# my_function()

## Describe the Problem - Write your answers as comments:
## 1. What is the for loop doing?
## 2. When is the function meant to print "You got it"?
## 3. What are your assumptions about the value of i?

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")


# my_function()

## Reproducing the Bug

# from random import randint
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(a = 1, b = 6)
# print(dice_images[dice_num])

# The code above occasionally gets an error.
# Changing the code so that it always reproduce an error.


# from random import randint
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(a = 0, b = 5)
# print(dice_images[dice_num])

# The list counts from zero. 0, 1, 2, 3, 4, 5..


## Play computer

# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# If you input 1994 on this code it will get a bug.
## 해당하는 조건이 없을 시 계속 넘어가고... 바가지같은 받아낼 것이 없으면 아무것도 출력하지 않음.

# year = int(input("What's your year of birth?"))

# if year > 1980 and year <= 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# 구글 쳐보니 94년생은 밀레니얼이라고...

# year = int(input("What's your year of birth?"))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# Angela says that 1994 is a Gen Z. lol

## Fix the Errors

# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")

# If you use some words like "twelve" instead of actual numbers it'll create an error.


# try:
#     age = int(input("How old are you?"))
# except ValueError:
#     print("You have typed in an invalid number. Please try again with a numerical response such as 12.")
#     age = int(input("How old are you?"))

# if age > 18:
#     print("You can drive at age {age}.")


# Fix the code so that you can get the actual value of the variable.

# try:
#     age = int(input("How old are you?\n"))
# except ValueError:
#     print("You have typed in an invalid number. Please try again with a numerical response such as 12.")
#     age = int(input("How old are you?\n"))
    
# if age > 18:
#     print(f"You can drive at age {age}.")


## Print Is Your Friend

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

## The results only show 0
## If we try debugging this using print to find out the reason

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page

# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(total_words)

## So the final code would be;


# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page

# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(total_words)


## Using a Debugger


# import random

# def add(n1, n2):
#     return n1 + n2

# def mutate(a_list): 
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1, 3) 
#         new_item = add(new_item, item) 
#         b_list.append(new_item)
        
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

## Using debug--

# import random

# def add(n1, n2):
#     return n1 + n2

# def mutate(a_list): # a_list : [1, 2, 3, 5, 8, 13] 
#     b_list = [] # b_list : []
#     new_item = 0 #new_item : 5
#     for item in a_list:
#         new_item = item * 2 
#         new_item += random.randint(1, 3) 
#         new_item = add(new_item, item) 
#     b_list.append(new_item)
#     print(b_list)

# mutate([1, 2, 3, 5, 8, 13])

## Coding exercise 12 : Debugging Odd or Even

# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
    
# --->

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."


## Coding exercise 13 : Debugging Leap Year
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 4000 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
    
# ------>
    
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False


## Coding Exercise 14 : Debugging FizzBuzz

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 or number % 5 == 0:
#             print("FizzBuzz")
#         if number % 3 == 0:
#             print("Fizz")
#         if number % 5 == 0:
#             print("Buzz")
#         else:
#             print([number])

# ---->

# def fizz_buzz(target):
#     for number in range(1, target + 1):
#         if number % 3 == 0 and number % 5 == 0:
#             print("FizzBuzz")
#         elif number % 3 == 0:
#             print("Fizz")
#         elif number % 5 == 0:
#             print("Buzz")
#         else:
#             print(number)

# ---------------End of Day 13 ------------------


## Day 14 : Higher Lower Game Project

# <Given data are the following;>

# logo = """
# .__    .__       .__                   
# |  |__ |__| ____ |  |__   ___________  
# |  |  \|  |/ ___\|  |  \_/ __ \_  __ \ 
# |   Y  \  / /_/  >   Y  \  ___/|  | \/ 
# |___|  /__\___  /|___|  /\___  >__|    
#      \/  /_____/      \/     \/        
                                       
#   ___________                          
#  /  _ \_  __ \                         
# (  <_> )  | \/                         
#  \____/|__|                            
                                       
# .__                                    
# |  |   ______  _  __ ___________       
# |  |  /  _ \ \/ \/ // __ \_  __ \      
# |  |_(  <_> )     /\  ___/|  | \/      
# |____/\____/ \/\_/  \___  >__|         
#                         \/          

# """

# vs = """
             
# ___  ________
# \  \/ /  ___/
#  \   /\___ \ 
#   \_//____  >
#           \/ 

# """


# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
#     {
#         'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kylie Jenner',
#         'follower_count': 172,
#         'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 167,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 149,
#         'description': 'Footballer',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Beyoncé',
#         'follower_count': 145,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 138,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'National Geographic',
#         'follower_count': 135,
#         'description': 'Magazine',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 133,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Taylor Swift',
#         'follower_count': 131,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kendall Jenner',
#         'follower_count': 127,
#         'description': 'Reality TV personality and Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Jennifer Lopez',
#         'follower_count': 119,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Nicki Minaj',
#         'follower_count': 113,
#         'description': 'Musician',
#         'country': 'Trinidad and Tobago'
#     },
#     {
#         'name': 'Nike',
#         'follower_count': 109,
#         'description': 'Sportswear multinational',
#         'country': 'United States'
#     },
#     {
#         'name': 'Khloé Kardashian',
#         'follower_count': 108,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Miley Cyrus',
#         'follower_count': 107,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Katy Perry',
#         'follower_count': 94,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kourtney Kardashian',
#         'follower_count': 90,
#         'description': 'Reality TV personality',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kevin Hart',
#         'follower_count': 89,
#         'description': 'Comedian and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Ellen DeGeneres',
#         'follower_count': 87,
#         'description': 'Comedian',
#         'country': 'United States'
#     },
#     {
#         'name': 'Real Madrid CF',
#         'follower_count': 86,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'FC Barcelona',
#         'follower_count': 85,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'Rihanna',
#         'follower_count': 81,
#         'description': 'Musician and businesswoman',
#         'country': 'Barbados'
#     },
#     {
#         'name': 'Demi Lovato',
#         'follower_count': 80,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': "Victoria's Secret",
#         'follower_count': 69,
#         'description': 'Lingerie brand',
#         'country': 'United States'
#     },
#     {
#         'name': 'Zendaya',
#         'follower_count': 68,
#         'description': 'Actress and musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Shakira',
#         'follower_count': 66,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Drake',
#         'follower_count': 65,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Chris Brown',
#         'follower_count': 64,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'LeBron James',
#         'follower_count': 63,
#         'description': 'Basketball player',
#         'country': 'United States'
#     },
#     {
#         'name': 'Vin Diesel',
#         'follower_count': 62,
#         'description': 'Actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cardi B',
#         'follower_count': 67,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'David Beckham',
#         'follower_count': 82,
#         'description': 'Footballer',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Billie Eilish',
#         'follower_count': 61,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Timberlake',
#         'follower_count': 59,
#         'description': 'Musician and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'UEFA Champions League',
#         'follower_count': 58,
#         'description': 'Club football competition',
#         'country': 'Europe'
#     },
#     {
#         'name': 'NASA',
#         'follower_count': 56,
#         'description': 'Space agency',
#         'country': 'United States'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 56,
#         'description': 'Actress',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Shawn Mendes',
#         'follower_count': 57,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Virat Kohli',
#         'follower_count': 55,
#         'description': 'Cricketer',
#         'country': 'India'
#     },
#     {
#         'name': 'Gigi Hadid',
#         'follower_count': 54,
#         'description': 'Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Priyanka Chopra Jonas',
#         'follower_count': 53,
#         'description': 'Actress and musician',
#         'country': 'India'
#     },
#     {
#         'name': '9GAG',
#         'follower_count': 52,
#         'description': 'Social media platform',
#         'country': 'China'
#     },
#     {
#         'name': 'Ronaldinho',
#         'follower_count': 51,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'Maluma',
#         'follower_count': 50,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Camila Cabello',
#         'follower_count': 49,
#         'description': 'Musician',
#         'country': 'Cuba'
#     },
#     {
#         'name': 'NBA',
#         'follower_count': 47,
#         'description': 'Club Basketball Competition',
#         'country': 'United States'
#     }
# ]

# -----end of given data. now get to work.-----


# TODO's
# Display art
# Generate a random account from the game data
# Format the account data into printable format.
# Ask user for a guess.

# Check if user is correct.
# Get follower count for each account.
# User if statement to check if user is correct.

# Give user feedback on their guess.
# Score keeping.
# Make the game repeatable.
# Making account at position B become the next account at position A.

# ----------- Angela's solution --------------------------------

# def format_data(account):
#     """Format the account data into printable format."""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"


# ## Check if user is correct.
# def check_answer(user_guess, a_followers, b_followers):
#     """Take a user's guess and the follower counts and returns if they got it right."""
#     if a_followers > b_followers:
#         if user_guess == "a":
#             return True
#         else:
#             return False
#     else:
#         if user_guess == "b":
#             return True
#         else:
#             return False

# ## The actual shorter version of the code above
# # def check_answer(user_guess, a_followers, b_followers):
# #     """Take a user's guess and the follower counts and returns if they got it right."""
# #     if a_followers > b_followers:
# #         return user_guess == "a"
# #     else:
# #         return user_guess == "b"
        

# ## Display art
# import random
# print(logo)
# score = 0
# game_should_continue = True
# # Making account at position B become the next account at position A.
# account_b = random.choice(data)


# # Make the game repeatable. 
# while game_should_continue:
#     ## Generate a random account from the game data
#     # Making account at position B become the next account at position A.
#     account_a = account_b
#     account_b = random.choice(data)
#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Compare B: {format_data(account_b)}.")

#     ## Ask user for a guess.
#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     ## Clear the screen, print the logo again
#     print("\n" * 20)
#     print(logo)


#     ## Get follower count for each account.
#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]

#     ## User if statement to check if user is correct.
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     # Give user feedback on their guess.
#     # Score keeping.
#     if is_correct:
#         score += 1
#         print(f"You're right! Current score {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score : {score}")
#         game_should_continue = False
    

## <Final code solution>--------------------------------


# logo = """
# .__    .__       .__                   
# |  |__ |__| ____ |  |__   ___________  
# |  |  \|  |/ ___\|  |  \_/ __ \_  __ \ 
# |   Y  \  / /_/  >   Y  \  ___/|  | \/ 
# |___|  /__\___  /|___|  /\___  >__|    
#      \/  /_____/      \/     \/        
                                       
#   ___________                          
#  /  _ \_  __ \                         
# (  <_> )  | \/                         
#  \____/|__|                            
                                       
# .__                                    
# |  |   ______  _  __ ___________       
# |  |  /  _ \ \/ \/ // __ \_  __ \      
# |  |_(  <_> )     /\  ___/|  | \/      
# |____/\____/ \/\_/  \___  >__|         
#                         \/          

# """

# vs = """
             
# ___  ________
# \  \/ /  ___/
#  \   /\___ \ 
#   \_//____  >
#           \/ 

# """


# data = [
#     {
#         'name': 'Instagram',
#         'follower_count': 346,
#         'description': 'Social media platform',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cristiano Ronaldo',
#         'follower_count': 215,
#         'description': 'Footballer',
#         'country': 'Portugal'
#     },
#     {
#         'name': 'Ariana Grande',
#         'follower_count': 183,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Dwayne Johnson',
#         'follower_count': 181,
#         'description': 'Actor and professional wrestler',
#         'country': 'United States'
#     },
#     {
#         'name': 'Selena Gomez',
#         'follower_count': 174,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kylie Jenner',
#         'follower_count': 172,
#         'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kim Kardashian',
#         'follower_count': 167,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Lionel Messi',
#         'follower_count': 149,
#         'description': 'Footballer',
#         'country': 'Argentina'
#     },
#     {
#         'name': 'Beyoncé',
#         'follower_count': 145,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Neymar',
#         'follower_count': 138,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'National Geographic',
#         'follower_count': 135,
#         'description': 'Magazine',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Bieber',
#         'follower_count': 133,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Taylor Swift',
#         'follower_count': 131,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kendall Jenner',
#         'follower_count': 127,
#         'description': 'Reality TV personality and Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Jennifer Lopez',
#         'follower_count': 119,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Nicki Minaj',
#         'follower_count': 113,
#         'description': 'Musician',
#         'country': 'Trinidad and Tobago'
#     },
#     {
#         'name': 'Nike',
#         'follower_count': 109,
#         'description': 'Sportswear multinational',
#         'country': 'United States'
#     },
#     {
#         'name': 'Khloé Kardashian',
#         'follower_count': 108,
#         'description': 'Reality TV personality and businesswoman',
#         'country': 'United States'
#     },
#     {
#         'name': 'Miley Cyrus',
#         'follower_count': 107,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': 'Katy Perry',
#         'follower_count': 94,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kourtney Kardashian',
#         'follower_count': 90,
#         'description': 'Reality TV personality',
#         'country': 'United States'
#     },
#     {
#         'name': 'Kevin Hart',
#         'follower_count': 89,
#         'description': 'Comedian and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Ellen DeGeneres',
#         'follower_count': 87,
#         'description': 'Comedian',
#         'country': 'United States'
#     },
#     {
#         'name': 'Real Madrid CF',
#         'follower_count': 86,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'FC Barcelona',
#         'follower_count': 85,
#         'description': 'Football club',
#         'country': 'Spain'
#     },
#     {
#         'name': 'Rihanna',
#         'follower_count': 81,
#         'description': 'Musician and businesswoman',
#         'country': 'Barbados'
#     },
#     {
#         'name': 'Demi Lovato',
#         'follower_count': 80,
#         'description': 'Musician and actress',
#         'country': 'United States'
#     },
#     {
#         'name': "Victoria's Secret",
#         'follower_count': 69,
#         'description': 'Lingerie brand',
#         'country': 'United States'
#     },
#     {
#         'name': 'Zendaya',
#         'follower_count': 68,
#         'description': 'Actress and musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Shakira',
#         'follower_count': 66,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Drake',
#         'follower_count': 65,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Chris Brown',
#         'follower_count': 64,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'LeBron James',
#         'follower_count': 63,
#         'description': 'Basketball player',
#         'country': 'United States'
#     },
#     {
#         'name': 'Vin Diesel',
#         'follower_count': 62,
#         'description': 'Actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'Cardi B',
#         'follower_count': 67,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'David Beckham',
#         'follower_count': 82,
#         'description': 'Footballer',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Billie Eilish',
#         'follower_count': 61,
#         'description': 'Musician',
#         'country': 'United States'
#     },
#     {
#         'name': 'Justin Timberlake',
#         'follower_count': 59,
#         'description': 'Musician and actor',
#         'country': 'United States'
#     },
#     {
#         'name': 'UEFA Champions League',
#         'follower_count': 58,
#         'description': 'Club football competition',
#         'country': 'Europe'
#     },
#     {
#         'name': 'NASA',
#         'follower_count': 56,
#         'description': 'Space agency',
#         'country': 'United States'
#     },
#     {
#         'name': 'Emma Watson',
#         'follower_count': 56,
#         'description': 'Actress',
#         'country': 'United Kingdom'
#     },
#     {
#         'name': 'Shawn Mendes',
#         'follower_count': 57,
#         'description': 'Musician',
#         'country': 'Canada'
#     },
#     {
#         'name': 'Virat Kohli',
#         'follower_count': 55,
#         'description': 'Cricketer',
#         'country': 'India'
#     },
#     {
#         'name': 'Gigi Hadid',
#         'follower_count': 54,
#         'description': 'Model',
#         'country': 'United States'
#     },
#     {
#         'name': 'Priyanka Chopra Jonas',
#         'follower_count': 53,
#         'description': 'Actress and musician',
#         'country': 'India'
#     },
#     {
#         'name': '9GAG',
#         'follower_count': 52,
#         'description': 'Social media platform',
#         'country': 'China'
#     },
#     {
#         'name': 'Ronaldinho',
#         'follower_count': 51,
#         'description': 'Footballer',
#         'country': 'Brasil'
#     },
#     {
#         'name': 'Maluma',
#         'follower_count': 50,
#         'description': 'Musician',
#         'country': 'Colombia'
#     },
#     {
#         'name': 'Camila Cabello',
#         'follower_count': 49,
#         'description': 'Musician',
#         'country': 'Cuba'
#     },
#     {
#         'name': 'NBA',
#         'follower_count': 47,
#         'description': 'Club Basketball Competition',
#         'country': 'United States'
#     }
# ]


# def format_data(account):
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}"


# def check_answer(user_guess, a_followers, b_followers):
#     if a_followers > b_followers:
#         if user_guess == "a":
#             return True
#         else:
#             return False
#     else:
#         if user_guess == "b":
#             return True
#         else:
#             return False


# import random
# print(logo)
# score = 0
# game_should_continue = True
# account_b = random.choice(data)



# while game_should_continue:

#     account_a = account_b
#     account_b = random.choice(data)
#     if account_a == account_b:
#         account_b = random.choice(data)

#     print(f"Compare A: {format_data(account_a)}.")
#     print(vs)
#     print(f"Compare B: {format_data(account_b)}.")

#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     print("\n" * 20)
#     print(logo)


#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]

#     is_correct = check_answer(guess, a_follower_count, b_follower_count)


#     if is_correct:
#         score += 1
#         print(f"You're right! Current score {score}")
#     else:
#         print(f"Sorry, that's wrong. Final score : {score}")
#         game_should_continue = False
    

# ---- end of day 14------

## Day 15 Intermediate - Local Development Environment setup & the Coffee Machine

# COFFEE MACHINE 

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water" : 300,
#     "milk" : 200,
#     "coffee" : 100,
# }

# TODO
## VScode에서는 TODO만 볼수 있는 탭이 없고, 보려면 확장 프로그램을 설치해야 하나 이마저도 search 옵션을 사용해야 함. 참고하면 될듯


## Coffee Machine Program Requirements ##

## 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

## 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.

## 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

## 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

## 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

## 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.

## 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.

# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0

# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.

# ----------------------<Angela's solution>------------------------


# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water" : 300,
#     "milk" : 200,
#     "coffee" : 100,
# }

# def is_resource_sufficient(order_ingredients):
#     """Returns True when orders can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True

# def process_coins():
#     """Returns the total cacluated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("How many quarters?: ")) * 0.25
#     total += int(input("How many dimes?: ")) * 0.1
#     total += int(input("How many nickles?: ")) * 0.05
#     total += int(input("How many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} on change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
    
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️")


# is_on = True

# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])

# # -------Final complete code----------
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water" : 300,
#     "milk" : 200,
#     "coffee" : 100,
# }

# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True

# def process_coins():
#     print("Please insert coins.")
#     total = int(input("How many quarters?: ")) * 0.25
#     total += int(input("How many dimes?: ")) * 0.1
#     total += int(input("How many nickles?: ")) * 0.05
#     total += int(input("How many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} on change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
    
# def make_coffee(drink_name, order_ingredients):
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️")


# is_on = True

# while is_on:
#     choice = input("What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])

# ----------End of Day 15--------------

# Day 16 : Intermediate - Object Oriented Programming (OOP)

# As the code gets more complex and having more functions and variables, it gets really hard to track on what's happening on our code.(Most code that I tried coding is Procedural Programming)
# Procedural Programming is mostly from earlier stages of programming.

# Object Oriented Programming is to put a big project into smaller pieces, the best way to explain it is to think of it as a restaurant - and def each waiter / receptionist / chef / cleaner etc, and have a manager that takes care all of these staff. It's basically about making it scalable for a more large and complex project.

## Waiter
    # <attributes> : Basically a variable - that's associated with a module object.(attached)
    # has : is_holding_plate = True 
            # tables_resonsible = [4, 5, 6]

    # <methods> : Because it's a function that a particular object can do.
    # does : def take_order(table, order):
            ## takes order to chef
            # def take_payment(amount):
            ## add money to restaurant

## We'll gonna see them again and again, so keep them in mind.(In OOP, we're trying to model real likfe objects and these objects have things that they can do things)
## Have things - variable, as attributes
## Do things - function, as methods

## Constructing Objects and Accessomg their Attributes and Methods

# car = CarBlueprint()
# In this case car is the object, CarBlueprint is the class.

# import another_module
# print(another_module.another_variable)


# import turtle
# timmy = turtle.Turtle()

## or

# from turtle import Turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# from turtle import Screen
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

## car.stop() # car is the object, stop() is the method

## Python Packages

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# print(table)

# ## Manually changing table style
# table.align = "l"

# print(table)

## Building the Coffee Machine with OOP -------------
# <for proper documentation and exercise, look up the folder oop-coffee-machine-start's main.py file>

# from menu import Menu
# from menu import MenuItem
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine

# # TODO-1 :  print report

# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()


# money_machine.report()
# coffee_maker.report()

# # TODO-2 : check resources sufficient
# # TODO-3 : process coins
# # TODO-4 : Check transaction successful?
# is_on = True
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options})")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
#             coffee_maker.make_coffee(drink)


# --------End of day 16--------------
# Day 17 : Intermediate - The Quiz Project & The Benefits of OOP--------------

# Class is a Blueprint for creating objects.
# In this lession we'll be building our own class


# Different types of class namings;
# PascalCase : every Word Starts with Capital Letter
# camelCase : first word starts with lowercase letter, then every word starts with Capital Letter
# snake_case : every word is lowercase, and words are separated by underscores(_)
# In python most classes are named in PascalCase or snake_case

## Constructor
# -> It's the part of the blueprint that allows us to specifiy what should happen when we create the object from the class.
# -> In python, the constructor is always named __init__ (double underscores before and after init)
# -> The __init__ method is called automatically every time the class is being used to create a new object.

# class car:
#     def __init__(self, seats):
#         self.seats = seats

# my_car.seats = 5

## Method

# class Car:
#     def enter_race_mode():
#         self.seats = 2
    
# my_car.enter_race_mode()

## Quiz Project

# Attributes - text, answer
# new_q = Question('2+3=5", "True")

# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the African Elephant.", "answer": "False"},
#     {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
#     {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
#     {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
#     {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
#     {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
#     {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
#     {"text": "Google was originally called 'Backrub'.", "answer": "True"},
#     {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
#     {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
# ]

# ## Create a Question class with an __init__(): method with two attributes: text and answer.
# class Question:
#     def __init__(self, q_text, q_answer):
#         self.text = q_text
#         self.answer = q_answer

# # new_q = Question("sdfsdf", "False")
# # print(new_q.text)
# # print(new_q.answer)

# class QuizBrain:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.question_list = q_list
#         self.score = 0
#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)
    

#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
#         self.check_answer(user_answer, current_question.answer)

#     def check_answer(self, user_answer, correct_answer):
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right!")
#         else:
#             print("That's wrong.")
#         print(f"The correct answer was: {correct_answer}.")
#         print(f"Your current score is: {self.score}/{self.question_number}.")
#         print("\n")

# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain

# question_bank = []
# for question in question_data:
#     question_text = question["text"]
#     question_answer = question["answer"]
#     new_question = Question(q_text = question_text, q_answer = question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")


## -------End of day 17--------------

## Day 18: Intermediate - Turtle & the Graphical User Interface (GUI) --------------------------------
# Turtle Graphics, Tuples and Inporting Modules

# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("deepskyblue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# screen = Screen()
# screen.exitonclick()


## Turtle Challenge 1 : Draw a Square
# <my solution>
# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("deepskyblue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# screen = Screen()
# screen.exitonclick()

# <angela's solution>
# from turtle import Turtle, Screen

# tim = Turtle()

# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# screen = Screen()
# screen.exitonclick()

## Importing Modules

# import turtle

# tim = turtle.Turtle()

# VERSUS

# from turtle import Turtle
# # Keyword / Module Name / Keyword / Thing in Module

# tim = Turtle()
# tom = Turtle()
# terry = Turtle()
# # It's easier to code and import multiple things from the same module this way.

# A way to import everything
# from turtle import * (the asterisk means everything)

# from turtle import *
# disadvantage : it's hard to know which module a function came from, especially when there are many modules being imported.
# So it's advised to import only the things that are needed, not everything.

## Aliasing Modules
# import turtle as t
# Keyword / Module name / Keyword / Alias name
# tim = t.Turtle()
# It a way to shorten the module name for easier typing.
## Installing modules
# import heroes
# -> this will cause an error as the module is not installed yet.
# (in VS, type pip install heroes to the terminal to install the module)

# import heroes
# print(heroes.gen())


## Turtle Challenge 2 - Draw a Dashed Line

# import turtle as t
# tim = t.Turtle()



# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

## Turtle Challenge 3 - Drawing Different Shapes

# import turtle as t
# import random

# tim = t.Turtle()

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# # num_sides = 5 
# # for _ in range(num_sides):
# #     angle = 360 / num_sides
# #     tim.forward(100)
# #     tim.right(angle)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

## Turtle Challenge 4 - Gerenate a Random Walk

# import turtle as t
# import random

# tim = t.Turtle()

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")


# for _ in range(200):
#     tim.color(random.choice(colors))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


## Python Tuples and How to Generate Random RGB Colors

# Tuples = (1, 3, 8)
# my_tuple[2] would be 3
# but in Tuple, you cannot change the value at all, it's immutable.
# When you're using Tuples, you use it for when you want to stay constant and don't want someone to change it by accident.

# But if you want to change it into a list, you can do this:
# list(my_tuple)


# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255) # 0 to 255 RGB color mode

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

## Turtle Challenge 5 - Draw a Spirograph


# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255) # 0 to 255 RGB color mode

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# tim.speed("fastest")

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)

# draw_spirograph(5)

# screen = t.Screen()
# screen.exitonclick()

### Day 18 Project : The Hirst Painting Project ##
## How to extract RGB Values from Images

# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst-painting(day_18)/image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

# # Extracted RGB colors from the image
# color_list = [(203, 165, 109), (150, 72, 48), (239, 245, 240), (232, 235, 241), (222, 202, 137), (171, 152, 41), (52, 93, 124), (135, 32, 23), (133, 162, 184), (198, 92, 72), (49, 123, 90), (14, 98, 74), (146, 178, 147), (69, 49, 41), (234, 176, 166), (162, 142, 157), (55, 45, 50), (150, 19, 23), (113, 75, 77), (185, 205, 174), (22, 82, 86), (48, 65, 81), (45, 61, 73), (90, 144, 126), (219, 177, 181), (108, 127, 154), (194, 83, 86), (178, 190, 208)]


# import turtle as turtle_module
# import random

# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(203, 165, 109), (150, 72, 48), (239, 245, 240), (232, 235, 241), (222, 202, 137), (171, 152, 41), (52, 93, 124), (135, 32, 23), (133, 162, 184), (198, 92, 72), (49, 123, 90), (14, 98, 74), (146, 178, 147), (69, 49, 41), (234, 176, 166), (162, 142, 157), (55, 45, 50), (150, 19, 23), (113, 75, 77), (185, 205, 174), (22, 82, 86), (48, 65, 81), (45, 61, 73), (90, 144, 126), (219, 177, 181), (108, 127, 154), (194, 83, 86), (178, 190, 208)]

# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100

# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)

#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)


# screen = turtle_module.Screen()
# screen.exitonclick()
# ## -------End of day 18--------------

## Day 19 : Intermediate - Instances, State and Higher Order Functions

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()

## Functions as Inputs

# def function_a(something):
#     #Do this with something
#     #Then do this
#     #Finally do this

# def function_b():
#     #Do this

# function_a(function_b)
# -> function_b is being passed into function_a as an input.
# -> function_a can now use function_b inside its own function body.

# ex)

# def add(n1, n2):
#     return n1 + n2

# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# def calculator(n1, n2, func):
#     return func(n1, n2)

# result = calculator(2, 3, add)
# print(result)

# result = calculator(2, 3, subtract)
# print(result)

# result = calculator(2, 3, multiply)
# print(result)

# result = calculator(2, 3, divide)
# print(result)

# In this case, the calculator is the higher order function
# This is commonly used in Python unlike other programming languages.

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)

# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear_screen, "c")
# screen.exitonclick()

## Object State and Instances

## OBJECT ## CLASS
# timmy = Turtle() ## INSTANCE (example of the object)
# tommy = Turtle() ## INSTANCE (example of the object)

# timmy.color = green
# tommy.color = purple
# (each objects can have different attributes and can be performing different methods independently)

## Understanding the Turtle Coordinate System

# from turtle import Turtle, Screen

# screen = Screen()
# screen.setup(width = 500, height = 400)
# user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -40, -10, 20, 50, 80]


# for turtle_index in range(0, 6):
#     tim = Turtle(shape="turtle")
#     tim.color(colors[turtle_index])
#     tim.penup()
#     tim.goto(x = -230, y = y_positions[turtle_index])


# screen.exitonclick()

## Day 19 Project : Turtle Race

# import random
# from turtle import Turtle, Screen

# is_race_on = False
# screen = Screen()
# screen.setup(width = 500, height = 400)
# user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -40, -10, 20, 50, 80]
# all_turtles =[]

# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.penup()
#     new_turtle.color(colors[turtle_index])
#     new_turtle.goto(x = -230, y = y_positions[turtle_index])
#     all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! The {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost! The {winning_color} turtle is the winner!")
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)


# screen.exitonclick()

## ---------------- End of Day 19 --------------------------------

## Day 20 : Intermediate - Build the Snake Game Part 1 : Animation & Coordinates
# Day 20 Goals:
#     1) Create a snake body
#     2) Move the snake
#     3) Control the snake(keyboard controls)
# Day 21 Goals:
#     4) Detect collision with food
#     5) Create a scoreboard
#     6) Detect collision with wall
#     7) Detect collision with tail

## 0) Making a base
# from turtle import Screen, Turtle

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")

# screen.exitonclick()

## 1) Create a snake body
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(x = -20, y = 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(x = -40, y = 0)

# or using loop
# starting_positions =[(0, 0), (-20, 0), (-40, 0)]

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)

# <current code>
# from turtle import Screen, Turtle

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")

# starting_positions =[(0, 0), (-20, 0), (-40, 0)]

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.goto(position)



# screen.exitonclick()



## 2) Move the snake

# from turtle import Screen, Turtle
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# starting_positions =[(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     for seg_num in range(len(segments) - 1, 0, -1): #(start, stop, step)
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)


# screen.exitonclick()

## 3) Create a Snake Class & Move to OOP


## The following is the snake.py (Snake class)
# from turtle import Turtle
# STARTING_POSITIONS =[(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20

# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
    
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             new_segment = Turtle("square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
    
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1): #(start, stop, step)
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.segments[0].forward(MOVE_DISTANCE)

## And the following is the main.py

# from turtle import Screen, Turtle
# from snake import Snake
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()

# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()


# screen.exitonclick()

## 4) How to control the snake using Keystrokes

## main.py
# from turtle import Screen, Turtle
# from snake import Snake
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")



# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()


# screen.exitonclick()

## snake.py

# from turtle import Turtle
# STARTING_POSITIONS =[(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0

# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
    
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             new_segment = Turtle("square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
    
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1): #(start, stop, step)
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)

#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
    
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
    
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)

#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)


## End of Day 20 (The Snake Game Project continues...) ----
## DAY 21 : Build the Snake Game Part 2 : Inheritance and List Slicing


## Class Inheritance

# class Animal:
#     def __init__(self):
#       self.num_eyes = 2

#     def breathe(self):
#        print("Inhale, exhale.")


# class Fish(Animal):  # This is inheritance
#     def __init__(self):
#        super().__init__()
   
#     def swim(self):
#        print("moving in water.")

# nemo = Fish()
# nemo.swim()
# nemo.breathe()
# print(nemo.num_eyes)

# So now the object that's created from the Fish class now has access to all the attributes and methods from the superclass that inherited from the animal class.

# class Animal:
#     def __init__(self):
#       self.num_eyes = 2

#     def breathe(self):
#        print("Inhale, exhale.")


# class Fish(Animal):  # This is inheritance
#     def __init__(self):
#        super().__init__()

#     def breathe(self):
#        super().breathe()
#        print("doing this underwater.")
   
#     def swim(self):
#        print("moving in water.")

# nemo = Fish()
# nemo.breathe()

## This is an example to use the existing class and build more on top of it without editing anything.


## Detect Collisions with Food

## Make a new py file called "Food.py"

# from turtle import Turtle
# import random

# class Food(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
#         self.color("blue")
#         self.speed("fastest")
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)

## "main.py"

# from turtle import Screen
# from snake import Snake
# from food import Food
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()


# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")



# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()


# screen.exitonclick()

## So now at this point the food is randomly generated.

## Food.py(Refreshing the food when it's touched)
# from turtle import Turtle
# import random

# class Food(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
#         self.color("blue")
#         self.speed("fastest")
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)
#         self.refresh()

#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)

## Main.py
# from turtle import Screen
# from snake import Snake
# from food import Food
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()


# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")



# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()

#     # Detect collision with food.
#     if snake.head.distance(food) < 15:
#         food.refresh()


# screen.exitonclick()

## Create a Scoreboard and Keep Score

# Create a new class called Scoreboard.py

# from turtle import Turtle
# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))
#         self.hideturtle()

# 

# main.py
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()

#     if snake.head.distance(food) < 15:
#         food.refresh()


# screen.exitonclick()

## Scoreboard.py

# from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Arial", 24, "normal")

# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#             self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()

# Scoreboard.py
# from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Arial", 24, "normal")

# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#             self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

#     def game_over(self):
#          self.goto(0,0)
#          self.write("GAME OVER", align = ALIGNMENT, font = FONT)


#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()



# main.py

# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     if snake.head.distance(food) < 15:
#         food.refresh()
#         scoreboard.increase_score()

#     #Detect collision with wall
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()


# screen.exitonclick()

## Detect Collisions with your own tail

# main.py
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     # Detect collision with food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#     #Detect collision with wall
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()

#     #Detech collision with tail
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
#     # if head collides with any segment in the tail:
#         #trigger game_over

# screen.exitonclick()

# ----Final code---------
## main.py
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     # Detect collision with food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#     #Detect collision with wall
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()

#     #Detech collision with tail
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
#     # if head collides with any segment in the tail:
#         #trigger game_over

# screen.exitonclick()

## snake.py

# from turtle import Turtle
# STARTING_POSITIONS =[(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0

# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0]
    
#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             self.add_segment(position)

#     def add_segment(self, position):
#         new_segment = Turtle("square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)    

#     def extend(self):
#         self.add_segment(self.segments[-1].position())
    
    
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1): #(start, stop, step)
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)

#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)
    
#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)
    
#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)

#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)

## food.py

# from turtle import Turtle
# import random

# class Food(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
#         self.color("blue")
#         self.speed("fastest")
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)
#         self.refresh()

#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(random_x, random_y)

## scoreboard.py
# from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Arial", 24, "normal")

# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 270)
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#             self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

#     def game_over(self):
#          self.goto(0,0)
#          self.write("GAME OVER", align = ALIGNMENT, font = FONT)


#     def increase_score(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()

## room for improvement(using slicing)
## How to slice lists and tuples in Python

# # slicing lists
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# print(piano_keys[2:5]) # -> c, d, e
# # This is the example of slicing.

# print(piano_keys[2:]) #-> c, d, e, f, g
# print(piano_keys[:5]) #-> a, b, c, d, e
# print(piano_keys[2:5:2]) # -> c, e
# print(piano_keys[::2]) # -> a, c, e, g
# print(piano_keys[::-1]) # inverted


# # It also works with tuples.
# piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# print(piano_tuple[2:5])

# ------------------------------
## Now coming back to the snake code so that we can minimise the snake game code.

# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)


# snake = Snake()
# food = Food()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# screen.update()

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()

#     # Detect collision with food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         scoreboard.increase_score()

#     #Detect collision with wall
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         scoreboard.game_over()

#     #Detech collision with tail
#     for segment in snake.segments[1:]: #This will exclude the tail.
#         if snake.head.distance(segment) < 10:
#             game_is_on = False
#             scoreboard.game_over()
#     # if head collides with any segment in the tail:
#         #trigger game_over

# screen.exitonclick()

## End of Day 21----------------------------------

## Day 22 - Intermediate - Build Pong : The famous Arcade Game

## Create the screen
# main.py


# from turtle import Screen

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")

# screen.exitonclick()

## Create and move a paddle
# from turtle import Screen, Turtle

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)

# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")

# game_is_on = True
# while game_is_on:
#     screen.update()
 
# screen.exitonclick()

## Create another paddle
# Paddle.py

# from turtle import Turtle

# class Paddle(Turtle):

#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)

#     def go_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)

#     def go_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)

# main.py
# from turtle import Screen, Turtle
# from paddle import Paddle

# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))


# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     screen.update()
 

# screen.exitonclick()

## Create the ball and make it move

# ball.py
# from turtle import Turtle

# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("White")
#         self.shape("circle")
#         self.penup()
    
#     def move(self):
#         new_x = self.xcor() + 10
#         new_y = self.ycor() + 10
#         self.goto(new_x, new_y)

# main.py
# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# import time


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()

# screen.exitonclick()


## Detect collision with wall and bounce

## ball.py
# from turtle import Turtle

# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("White")
#         self.shape("circle")
#         self.penup()
#         self.x_move = 10
#         self.y_move = 10
    
#     def move(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#         self.goto(new_x, new_y)


#     def bounce(self):
#         self.y_move *= -1

# main.py
# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# import time


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()

#     # Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#     # needs to bounce lol
#         ball.bounce()

# screen.exitonclick()

## Detect collision with the paddle
# Paddle.py
# from turtle import Turtle


# class Paddle(Turtle):

#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)

#     def go_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)

#     def go_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)


# main.py
# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# import time


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()

#     # Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#     # needs to bounce lol
#         ball.bounce_y()
    
#     # Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()

# screen.exitonclick()


## Detect when paddle misses
# ball.py

# from turtle import Turtle

# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("White")
#         self.shape("circle")
#         self.penup()
#         self.x_move = 10
#         self.y_move = 10
    
#     def move(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#         self.goto(new_x, new_y)


#     def bounce_y(self):
#         self.y_move *= -1

#     def bounce_x(self):
#         self.x_move *= -1
    
#     def reset_position(self):
#         self.goto(0, 0)
#         self.bounce_x()
    

# main.py
# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# import time


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()

#     # Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#     # needs to bounce lol
#         ball.bounce_y()
    
#     # Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()
    
#     # Detect R paddle misses
#     if ball.xcor() > 380:
#         ball.reset_position()

#     # Detect L paddle misses
#     if ball.xcor() < -380:
#         ball.reset_position()


# screen.exitonclick()

## Score Keeping and Changing the Ball Speed

# scoreboard.py
# from turtle import Turtle

# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.clear()
#         self.goto(-180, 200)
#         self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
#         self.goto(180, 200)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()
    
#     def r_point(self):
#         self.r_score += 1
#         self.update_scoreboard()

# main.py

# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
# import time


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#     ball.move()

#     # Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#     # needs to bounce lol
#         ball.bounce_y()
    
#     # Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()
    
#     # Detect R paddle misses
#     if ball.xcor() > 380:
#         ball.reset_position()
#         scoreboard.l_point()

#     # Detect L paddle misses
#     if ball.xcor() < -380:
#         ball.reset_position()
#         scoreboard.r_point()


# screen.exitonclick()

## Increase the speed & final code
## FINAL CODE
## ball.py

# from turtle import Turtle

# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("White")
#         self.shape("circle")
#         self.penup()
#         self.x_move = 10
#         self.y_move = 10
#         self.move_speed = 0.1
    
#     def move(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#         self.goto(new_x, new_y)


#     def bounce_y(self):
#         self.y_move *= -1

#     def bounce_x(self):
#         self.x_move *= -1
#         self.move_speed * 0.9
    
#     def reset_position(self):
#         self.goto(0, 0)
#         self.move_speed = 0.1
#         self.bounce_x()
    
## paddle.py

# from turtle import Turtle


# class Paddle(Turtle):

#     def __init__(self, position):
#         super().__init__()
#         self.shape("square")
#         self.color("white")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)

#     def go_up(self):
#         new_y = self.ycor() + 20
#         self.goto(self.xcor(), new_y)

#     def go_down(self):
#         new_y = self.ycor() - 20
#         self.goto(self.xcor(), new_y)

## scoreboard.py

# from turtle import Turtle

# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.clear()
#         self.goto(-180, 200)
#         self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
#         self.goto(180, 200)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()
    
#     def r_point(self):
#         self.r_score += 1
#         self.update_scoreboard()

## main.py
# from turtle import Screen, Turtle
# from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
# import time


# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# ball = Ball()
# scoreboard = Scoreboard()

# screen.listen()
# screen.onkey(r_paddle.go_up, "Up")
# screen.onkey(r_paddle.go_down, "Down")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# game_is_on = True
# while game_is_on:
#     time.sleep(ball.move_speed)
#     screen.update()
#     ball.move()

#     # Detect collision with wall
#     if ball.ycor() > 280 or ball.ycor() < -280:
#     # needs to bounce lol
#         ball.bounce_y()
    
#     # Detect collision with paddle
#     if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
#         ball.bounce_x()
    
#     # Detect R paddle misses
#     if ball.xcor() > 380:
#         ball.reset_position()
#         scoreboard.l_point()

#     # Detect L paddle misses
#     if ball.xcor() < -380:
#         ball.reset_position()
#         scoreboard.r_point()


# screen.exitonclick()

## End of Day 22 -----------------------------

## Day 23 - Intermediate - The Turtle Crossing Capstone Project

## The Turtle Crossing Game

# You'll need to know how to create classes, inherit classes, and using the objects, and the turtle coordinate system and the turtle game engine.


## Step 1 - Check out how the game play works
# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

# 3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

# 4. When the turtle collides with a car, it's game over and everything stops.

# ----------------------------------
## Step 2 - Break down the Problem

# The first step of creating any large project is to breakdown the problem into smaller, bite-sized chunks. Add the following comments to the starting code and try to tackle them one-by-one.

# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.

# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. If you get stuck, check the video walkthrough in Step 4.

# Detect when the turtle player collides with a car and stop the game if this happens. If you get stuck, check the video walkthrough in Step 5.

# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. If you get stuck, check the video walkthrough in Step 6.

# Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.

# # [main.py]
# import time
# from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)

# player = Player()
# car_manager = CarManager()
# scoreboard = Scoreboard()



# screen.listen()
# screen.onkey(player.go_up, "Up")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()

#     car_manager.create_car()
#     car_manager.move_cars()

#     # Detect collision with car
#     for car in car_manager.all_cars:
#         if car.distance(player) < 20: # collision
#             game_is_on = False
#             scoreboard.game_over()

#     # Detect successful crossing
#     if player.is_at_finish_line():
#         player.go_to_start()
#         car_manager.level_up()
#         scoreboard.increase_level()


# screen.exitonclick()

## [player.py]
# import time
# from turtle import Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.tracer(0)

# player = Player()
# car_manager = CarManager()
# scoreboard = Scoreboard()



# screen.listen()
# screen.onkey(player.go_up, "Up")


# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()

#     car_manager.create_car()
#     car_manager.move_cars()

#     # Detect collision with car
#     for car in car_manager.all_cars:
#         if car.distance(player) < 20: # collision
#             game_is_on = False
#             scoreboard.game_over()

#     # Detect successful crossing
#     if player.is_at_finish_line():
#         player.go_to_start()
#         car_manager.level_up()
#         scoreboard.increase_level()


# screen.exitonclick()

## [car_manager.py]

# from turtle import Turtle
# import random

# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10


# class CarManager:
    
#     def __init__(self):
#         self.all_cars = []
#         self.car_speed = STARTING_MOVE_DISTANCE

#     def create_car(self):
#         random_chance = random.randint(1, 6)
#         if random_chance == 1:
#             new_car = Turtle("square")
#             new_car.shapesize(stretch_wid=1, stretch_len=2)
#             new_car.penup()
#             new_car.color(random.choice(COLORS))
#             random_y = random.randint(-250, 250)
#             new_car.goto(300, random_y)
#             self.all_cars.append(new_car)

#     def move_cars(self):
#         for car in self.all_cars:
#             car.backward(self.car_speed)

#     def level_up(self):
#         self.car_speed += MOVE_INCREMENT

## [scoreboard.py]

# from turtle import Turtle

# FONT = ("Courier", 24, "normal")


# class Scoreboard(Turtle):

#     def __init__(self):
#         super().__init__()
#         self.level = 1
#         self.hideturtle()
#         self.penup()
#         self.goto(-280, 250)
#         self.update_scoreboard()


#     def update_scoreboard(self):
#         self.clear()
#         self.write(f"Level: {self.level}", align = "left", font = FONT)


#     def increase_level(self):
#         self.level += 1
#         self.update_scoreboard()

#     def game_over(self):
#         self.goto(0, 0)
#         self.write(f"GAME OVER", align = "center", font = FONT)

# ---------End of Day 23------------
## Day 24 - Intermediate -Files, Directories and Paths

