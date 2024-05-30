def game_choice():
    choice = input("Pick one of the games you would like to play. Here are your options: Number Guessing Game, Tic Tac Toe, Rock Paper Scissors, or Hangman. Enter your choice here: ")
    if choice == "Number Guessing Game":
        Num_guess_game()
    if choice == "Tic Tac Toe":
        Tic_Tac_Toe()
    if choice == "Rock Paper Scissors":
        RPS()
    if choice == "Hangman":
        Hangman()

game_choice()
