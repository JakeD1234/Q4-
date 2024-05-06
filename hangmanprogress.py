def get_some_letters(word):
    guessed_letters = []
    hidden_word = "_" * len(word)
    for letter in word:
        if letter not in guessed_letters:
            guessed_letters.append(letter)
    
    chosen_letter = random.choice(guessed_letters)
    updated_hidden_word = ""
    
    for index in range(len(word)):
        letter = word[index]
        if letter == chosen_letter:
            updated_hidden_word += letter
        else:
            updated_hidden_word += hidden_word[index]
    
    return updated_hidden_word
