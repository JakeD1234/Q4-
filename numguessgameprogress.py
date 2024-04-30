'''
Create a number guessing game. There user should have two options: 
  1. The computer chooses a number and the user guesses 
    or 
  2. the user user chooses a number and the computer guesses. 

Write a pseudo-code version of your program here between the triple quotes first:
User descides option 1 or 2 by typing 1 or 2

if option 1:
the computer chooses a number and the user guesses
the computer choses a random number between 1 and 100
if user guesses a number
the computer tells the user if the number is too high or too low
each guess counts as a try
the goal is to get the number in the least amount of tries
if it is guessed in less than 5 tries, the user wins
return You Win!
if it is guessed in more than 5 tries, the user loses
return You Lose!

if option 2:
the user chooses a number and the computer guesses
the user chooses a random number between 1 and 100
if computer guesses a number
the user tells the computer if the number is too high or too low
eahc guess counts as a try
the goal is to get the number in the least amount of tries
if it is guessed in less than 5 tries, the computer wins
return You Win!
if it is guessed in more than 5 tries, the user loses
return You Lose!
'''

import random

print("Welcome to the number guessing game!")
print("You have two options:")
print("1. The computer chooses a number and the user guesses")
print("2. The user chooses a number and the computer guesses")
option = int(input("Please choose option 1 or 2: "))
if option == 1:
    print("The computer chooses a number between 1 and 100")
    print("Try to guess the number in 5 tries or less")
    my_number = random.randrange(1,101)
    while True:
        user_input = int(input("Guess a number between 1 and 100: "))
        if user_input == my_number:
            print("You Win!")
            break
        if user_input > my_number:
            print("Too high")
        if user_input < my_number:
            print("Too low")

else:
    user_input = int(input("Please choose a number between 1 and 100: "))
    print("The computer will try to guess your number in 5 tries or less")
    my_number = random.randrange(1,101)
    too_high = 101
    too_low = 0
    while True:
        computer_guess = random.randrange(too_low,too_high)
        print("The computer guesses", computer_guess)
        if computer_guess == user_input:
            print("Computer wins!")
            break
        user_feedback = input("Is the number too high (h), too low (l), or correct (c)? ")
        if user_feedback == 'h':
          print("Too high")
          too_high = computer_guess
        elif user_feedback == 'l':
          print("Too low")
          too_low = computer_guess
