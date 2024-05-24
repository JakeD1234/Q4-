def start_hangman_game():
    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
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
