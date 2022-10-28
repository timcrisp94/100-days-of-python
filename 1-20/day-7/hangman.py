#Step 1 
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, 2)]

guess = input("Player, guess a letter ").lower()

for letter in chosen_word:
  if letter == guess: 
    print("True ")
  else: 
    print("False ")



