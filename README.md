# Q4-
project for quarter 4 
My project will have a couple 2 or more player mini games such as hangman, tic tac toe, a number guessing games, rock paper scissors

code from: https://www.makeuseof.com/python-game-hangman-create/?utm_source=flipboard&utm_content=topic%2Fadventuregame

import random
 
def get_random_word_from_wordlist():
    wordlist = []
 
    with open("hangman_wordlist.txt", 'r') as file:
        wordlist = file.read().split("\n")
 
    word = random.choice(wordlist)
    return word

    This code will help me get started by getting a randm word from a seperate linked file for the user to guess in the hangman game
