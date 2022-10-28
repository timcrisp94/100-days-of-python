import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, (len(word_list) - 1))]


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
print(display)

guess = input("Player, guess a letter ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
  letter = chosen_word[position]
  if letter == guess: 
    display[position] = letter

print(display)
 



