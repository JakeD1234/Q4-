# Q4-
project for quarter 4 
My project will have a couple 2 or more player mini games such as hangman, tic tac toe, a number guessing games, rock paper scissors, and maybe even more

def tic_tac_toe():

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
    
    tic_tac_toe()
    
    
    def number_guessing_game():
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
                  print("You Win!")
                  break
            
                    
            
    number_guessing_game()
    
    
    
    
    
    
