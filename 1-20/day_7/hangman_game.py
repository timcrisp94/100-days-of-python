import random
import hangman_words
from hangman_art import logo, stages

# generate a random word
word_list = hangman_words.word_list
chosen_word = word_list[random.randint(0, (len(word_list) - 1))]

print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# display
display = []
word_len = len(chosen_word)

# display as many blanks as letters in word
for _ in range(word_len):
  display += '_'

# lives and end_of_game
lives = 6
end_of_game = False

# start game
while not end_of_game:
  # ask the user to guess a letter
  guess = input("Player, guess a letter ").lower()

  if guess in display:
    print(f"You already guessed {guess}")

  # check guessed letter
  for position in range(word_len):
    letter = chosen_word[position]    
    if letter == guess:
      display[position] = letter
  
  # check if user is wrong 
  if guess not in chosen_word:
    lives -= 1
    print(f"{guess} is not in the word. You have {lives} lives left.\n{stages[lives]}")

  # join all the elements in the list and turn it into a string.
  print(f"{' '.join(display)}")

  # winning condition
  if "_" not in display:
    end_of_game = True
    print("You win!")

  # losing condition
  if lives == 0:
    end_of_game = True
    print(f"You lose! The word was {chosen_word}")
