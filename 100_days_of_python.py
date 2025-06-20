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


# Day 3 final project(Treasure Island)

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where do you want to go? ' \
'Type "left" or "right".\n').lower()
 # Using .lower() to make the input case-insensitive.
 # when you put \ before the ' it will not be treated as a string and will be treated as a character.

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. ' \
    'Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed. There is house with 3 doors. ' \
                        'One "red", one "yellow", and one "blue". Which color do you choose?\n').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else :
        print("You got attacked by a trout. Game Over.")

# <Format 1>
else :
    print("You fell into a hole. Game Over.")

#<Format 2>
# if choice1 == "right":
#     print("You fell into a hole. Game Over.")

#If you want to countinue the game, you'll use the first format rather than the second one.
