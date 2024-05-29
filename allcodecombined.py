#Display the indicated game based on what the user inputs by prompting them to choose between one of the four games







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

input("#___Welcome to the number guessing game! In this game you play against the computer to try and guess it's number in 5 tries or less(option 1) or the cumputer will try to guess your number(option 2)___#                  #___Would You like to begin?___# :")
print("Please Pick which version you wuld like to play:")
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
    user_input = int(input("Please choose your number between 1 and 100: "))
    print("The computer will try to guess your number and you will tell it if it is too high or too low")
    my_number = random.randrange(1,101)
    too_high = 101
    too_low = 0
    while True:
        computer_guess = random.randrange(too_low,too_high)
        print("The computer guesses", computer_guess)
        if computer_guess == user_input:
            print("Computer wins!")
            break
        user_feedback = input("Is the number too high? if so enter (h),Is the number too low? if so enter (l) ")
        if user_feedback == 'h':
          print("Too high")
          too_high = computer_guess
        elif user_feedback == 'l':
          print("Too low")
          too_low = computer_guess
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
print("Hello, welcome to Toc Tac Toe! This is a 2 player game, In order to play you need to choose a number from 0-8, 0 being the top left corner of the board, and 8 being the bottom left corner of the board. Enjoy!")

def make_move(board, player):
  move = int(input("Enter a number from 0-8: "))
  if board[move]==' ':
    board[move] = player
  return board

board = [" "," "," "," "," "," "," "," "," "]
move = 'X'
def has_a_win(board):
  if board[0] != ' ' and board[0] == board[3] and board[3] == board[6]:
    return True
  if board[0] != ' ' and board[0] == board[1] and board[1] == board[2]:
    return True
  if board[0] != ' ' and board[0] == board[4] and board[4] == board[8]:
    return True
  if board[1] != ' ' and board[1] == board[4] and board[4] == board[7]:
    return True
  if board[2] != ' ' and board[2] == board[5] and board[5] == board[8]:
    return True
  if board[3] != ' ' and board[3] == board[4] and board[4] == board[5]:
    return True
  if board[6] != ' ' and board[6] == board[7] and board[7] == board[8]:
    return True
  if board[2] != ' ' and board[2] == board[4] and board[4] == board[6]:
    return True

def display_board(board):
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print('---------')
  print(board[6] + " | " + board[7] + " | " + board[8])


while True:
  display_board(board)
  make_move(board, move)
  if has_a_win(board):
    display_board(board)
    print(move + " wins!")
    break


  if move == 'X': 
    move = 'O'
  else: 
    move = 'X'
    
    
    
    
    
    
    
    
    
print("Hello, welocme to Rock, Paper, Scissors. This is a single player game where you will play against the computer by entering Rock, Paper, or Scissors.")



import random
options = ["Rock", "Paper", "Scissors"]
user_choice = input("Please choose either Rock, Paper, or Scissors: ")
computer_choice = random.choice(options)

print("You chose: ", user_choice)
print("Computer chose: ", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")

elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You win!")

elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")

elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You win!")

else:
    print("Computer wins!")
    
    
    
    
    
    
    
    
import random

def get_random_word_from_wordlist():
    wordlist = []
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')
    word = random.choice(wordlist)
    return word

def guess_letters(word):
    letters = []
    temp = '_'*len(word)
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = random.choice(letters)
    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def draw_hangman(chances):
    if chances == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif chances == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif chances == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif chances == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    elif chances == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")

def start_hangman_game():
    word = get_random_word_from_wordlist()
    temp = guess_letters(word)
    Guesses = 7
    found = False
    while True:
        if Guesses == 0:
            print(f"Better luck next time, you lost :( the word was: {word}")
            break
        print("#___Try to Guess the word___#")
        print(temp, end='')
        print(f"\t(The word has {len(word)} letters)")
        print(f"Wrong Guesses left: {Guesses}")
        character = input("Please enter a letter from A-Z that you think might be in the word *(Hint: Start with vowels)*: ")
        if len(character) > 1 or not character.isalpha():
            print("Please enter a single alphabet only")
            continue
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            Guesses -= 1
        if '_' not in temp:
            print(f"\nCongratulations! You Won! The word was: {word}")
            print(f"You got the word with {7 - Guesses} wrong guess/guesses left")
            break
        else:
            draw_hangman(Guesses)
        print()

print("#___Hello, Welcome To Hangman___#")
while True:
    choice = input("#___Do you want to play?___# (yes/no): ")
    if 'yes' in choice.lower():
        start_hangman_game()
    elif 'no' in choice.lower():
        print('')
        break
    else:
        print("**Error, Please enter in yes or no**")
    print("\n")
