def start_hangman_game():
    word = get_random_word_from_wordlist()
    word = get_some_letters(word)
    chances = 7
    while True:
        if chances == 0:
            print(f"Sorry! You Lost, the word was: {word}")
            print("Game Over! Good try, better luck next time!")
            break
        print("Guess the word")
        print(word, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have: ")
        if len(character) > 1 or not character.isalpha():
            print("Guess any single letter from the alphabet!")
