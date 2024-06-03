def game_choice():
    choice = input("Pick one of the games you would like to play. Here are your options: NUMBER GUESSING GAME!(NGG), TIC TAC TOE!(TTT), ROCK PAPE SCISSORS!(RPS), or HANGMAN!(H). Enter your choice here: ")
    if choice == "NGG":
        Num_guess_game()
    if choice == "TTT":
        Tic_Tac_Toe()
    if choice == "RPS":
        RPS()
    if choice == "H":
        Hangman()





    
def Num_guess_game():
    
    import random
    
    input("#___WELCOME TO THE NUMBER GUESSING GAME! In this game you play against the computer to try and guess it's number in 5 tries or less(option 1) or the cumputer will try to guess your number(option 2)___#                              #___WOULD YOU LIKE TO BEGIN?___# :")
    print("*PLEASE CHOOSE THE VERSION  YOU WOULD LIKE TO PLAY*")
    print("1. The computer chooses a number and the user guesses")
    print("2. The user chooses a number and the computer guesses")
    option = int(input("PLEASE CHOOSE OPTION 1 OR 2: "))
    if option == 1:
        print("The computer chooses a number between 1 and 100")
        print("Try to guess the number in 5 tries or less")
        my_number = random.randrange(1,101)
        while True:
            user_input = int(input("Guess a number between 1 and 100: "))
            if user_input == my_number:
                print("YOU WIN!")
                break
            if user_input > my_number:
                print("TOO HIGH")
            if user_input < my_number:
                print("TOO LOW")
    
    else:
        user_input = int(input("PLEASE CHOOSE YOUR NUMBER, BETWEEN 1 AND 100: "))
        print("The computer will try to guess your number and you will tell it if it is too high or too low")
        my_number = random.randrange(1,101)
        too_high = 101
        too_low = 0
        while True:
            computer_guess = random.randrange(too_low,too_high)
            print("The computer guesses", computer_guess)
            if computer_guess == user_input:
                print("COMPUTER WINS!")
                break
            user_feedback = input("Is the number too high? if so enter (h),Is the number too low? if so enter (l) ")
            if user_feedback == 'h':
              print("TOO HIGH")
              too_high = computer_guess
            elif user_feedback == 'l':
              print("TOO LOW")
              too_low = computer_guess
        Num_guess_game()
          
          
          
          
          
          
          
         
          
          
          
          
          
          
          
          
          
def Tic_Tac_Toe():
    print("--------------------------------------------------------------------------------------------------------------")    
    print("HELLO, WELCOME TO RIC TAC TOE! This is a 2 player game, In order to play you need to choose a number from 0-8, 0 being the top left corner of the board, and 8 being the bottom Right corner of the board.(Go from Left to right by row) ENJOY!")
    
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
    Tic_Tac_Toe()

    
    
    
    
    
    
def RPS():
    print("--------------------------------------------------------------------------------------------------------------")
    print("HELLO, WELCOME TO ROCK PAPER SCISSORS! In this game you will play against the computer by entering Rock, Paper, or Scissors.")
    
    
    
    import random
    options = ["Rock", "Paper", "Scissors"]
    user_choice = input("Please choose either Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)
    
    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)
    if user_choice == computer_choice:
        print("IT'S A TIE!")
    
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("YOU WIN!")
    
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("YOU WIN!")
    
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("YOU WIN!")
    
    else:
        print("COMPUTER WINS!")
    RPS()
    
    
 
    
    
def Hangman():
    print("--------------------------------------------------------------------------------------------------------------")       
    print("HELLO, WELCOME TO HANGMAN! In this game the computer will choose a random work from the word list and you will do your best to guess it by choosing one letter at a time. Each guess you get wrong the hangman gets one more body part and when you get seven wrong you lose. GOOD LUCK!")
    import random
    
    def Random_word():
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
    
    def drawing(chances):
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
    
    def Begin_game():
        word = Random_word()
        temp = guess_letters(word)
        Guesses = 7
        found = False
        while True:
            if Guesses == 0:
                print(f"Better luck next time, you lost :( the word was: {word}")
                break
            print("*TRY TO GUESS THE SECRET WORD!*")
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
                drawing(Guesses)
            print()
    
    while True:
        choice = input("#___WOULD YOU LIKE TO BEGIN?___# (yes/no): ")
        if choice == "yes":
            Begin_game()

        Hangman()



game_choice()
